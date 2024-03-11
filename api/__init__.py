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
from ariadne.asgi.handlers import GraphQLTransportWSHandler

#create app starlette library
from starlette.applications import Starlette
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
    #allow CORS to conect in public networks
) , allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))

async def ref(request):
    ''' Info micro_service, useful to validate connection'''
    return JSONResponse({
        "Author": "auditando.co",
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
    debug=False, routes=routes, lifespan=lifespan, exception_handlers=exception_handlers
)
