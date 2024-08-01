'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Load app GraphQL Ariadne
'''
#to execute lifespan library
import contextlib

#call graphql ariadne library

from ariadne_graphql_modules import make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler, GraphQLHTTPHandler
from graphql import GraphQLFieldResolver, MiddlewareManager

#create app starlette library
from asgi_background import BackgroundTaskMiddleware, BackgroundTasks
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount, WebSocketRoute

# call queries and mutations
from .graphql import *
#Events socket
from api.resolvers.subscriptions import on_connect, on_disconnect
#call broadcaster memory
from .graphql.subscription import pubsub
#call info context
from .info_context import get_context_value
#Unexpected errors
from .error_exception import exception_handlers

import json
from http import HTTPStatus

from starlette.requests import Request
from starlette.responses import Response

from .resolvers.background import tasks_background

class CustomGraphQLHTTPHandler(GraphQLHTTPHandler):
    async def create_json_response(
        self,
        request: Request,  # pylint: disable=unused-argument
        result: dict,
        success: bool,
    ):
        bac= await tasks_background().exec(request.scope)
        print('custom:', bac) 
        status_code = HTTPStatus.OK if success else HTTPStatus.BAD_REQUEST
        content = json.dumps(
            result,
            ensure_ascii=False,
            allow_nan=False,
            indent=None,
            separators=(",", ":"),
        ).encode("utf-8")
        return Response(
            content,
            status_code=status_code,
            media_type="application/json"
        ) 

# load queries and mutations into a schema
schema = make_executable_schema(Query, Mutation, Subscription)

graphql = CORSMiddleware( GraphQL(
    #load schema in library
    schema=schema,
    #True in develop, False un production
    debug=False,
    #load request data and user id
    context_value=get_context_value,
    #load socket conecction
    websocket_handler=GraphQLTransportWSHandler( 
        on_connect=on_connect,
        on_disconnect=on_disconnect
    ), 
    http_handler=CustomGraphQLHTTPHandler(),    
    #allow CORS to conect in public networks
) , allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))


async def ref(request):
    ''' Info micro_service, useful to validate connection'''
    return JSONResponse({
        "Author": "Templates",
        "project": "GraphQL Backend",
        "version": "0.1",
        "contributor": ["Giovanni Junco"]
    }, status_code=200)

@contextlib.asynccontextmanager
async def lifespan(app):  
    '''Setup Starlette ASGI app with events to start and stop Broadcaster'''
    pubsub.connect
    yield    
    pubsub.disconnect

routes=[ 
        #Info micro_service
        Route('/', ref, methods=['GET']),
        #Routes to queries and mutations
        Mount("/graphql/", graphql),
        #Route to subscriptions
        WebSocketRoute("/graphql/", endpoint=graphql)
        ]
# initiate starlette app
app = Starlette(
    debug=False, routes=routes, lifespan=lifespan, 
    exception_handlers=exception_handlers,
    middleware=[Middleware(BackgroundTaskMiddleware)]
)
