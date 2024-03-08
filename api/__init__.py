'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Errors 500
'''
#get internal error info
import sys
#send dict in string
import json

#to execute lifespan
import contextlib

#Internal Error Handler
from starlette.exceptions import HTTPException
from starlette.requests import Request

#load Graphql ariadne
from ariadne_graphql_modules import make_executable_schema
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler

#create app starlette
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
from starlette.responses import PlainTextResponse
from starlette.routing import Route


from aiodataloader import DataLoader

from .graphql import *
from api.resolvers.subscriptions import on_connect, on_disconnect

from .graphql.subscription import pubsub

schema = make_executable_schema(Query, Mutation, Subscription)

async def get_users_redis(users_ids: list[int]) -> list[dict]:
    ''' data loader permite guradar informacion asyncrona en info context'''
    try:
        print('users_ids:', users_ids)
        return [{}]
    except:
        print(' -get_users_from_api',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return []

def get_context_value(request, data):
    ''' si no se quiere usar almacenamiento en cache: DataLoader(get_users_from_api, cache=False)'''
    user_agent = request.headers.get("user-agent", "guest").split(' ')[-1]
    token = request.headers.get("Authorization", "No_token")   
    query_name= data.get("operationName", "No_name") 
    client_ip= request.get("client", "No_ip") 
    print('HEADERS: ',user_agent,' **|',token, query_name, client_ip)
    
    return {
        "request":request,
        "user_loader": DataLoader(get_users_redis),
        'login_loader':DataLoader(get_users_redis),
        'license_loader':DataLoader(get_users_redis),
        'order_loader':DataLoader(get_users_redis),
        'user_token':25,
        'headers_token': token
    }

graphql = CORSMiddleware( GraphQL(
    schema=schema,
    logger="admin.graphql",
    debug=True,    
    context_value=get_context_value,
    websocket_handler=GraphQLTransportWSHandler( 
        on_connect=on_connect,
        on_disconnect=on_disconnect
    ), 
) , allow_origins=['*'], allow_methods=("GET", "POST", "OPTIONS"))

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]
#route testing
async def ref(request):
    ''' Info micro_service, useful to validate connection'''
    ref= json.dumps({
        "Author": "auditando.co",
        "project": "GraphQL Backend",
        "version": "0.1",
        "contributor": ["Giovanni Junco"]
    })
    return PlainTextResponse(ref)

@contextlib.asynccontextmanager
async def lifespan(app):  
    '''Setup Starlette ASGI app with events to start and stop Broadcaster'''
    pubsub.connect
    yield
    pubsub.disconnect

async def http_exception(request: Request, exc: HTTPException):
    print(" -*Internal Error..")
    return {"detail": exc.detail, "status_code":exc.status_code}

exception_handlers = {
    HTTPException: http_exception
}
app = Starlette(
    debug=True, routes=[ Route('/', ref, methods=['GET'])], lifespan=lifespan, exception_handlers=exception_handlers
    #on_startup=[pubsub.connect],
    #on_shutdown=[pubsub.disconnect]
)

