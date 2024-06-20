'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Queries config
'''
# get error system info - library
import sys
# Parent class ObjectType to define query, gpl method to make schema
from ariadne_graphql_modules  import ObjectType, gql
# Send http request to microservice
from api.resolvers import ResolverRequest
# detect error 500
from logs import get_error

# Load all query schemas
from .user import UserType, ItemStatusEnum, TokenType
from .search import SearchType
from .order import OrderType
from .license import LicenseType
from .notification import NotificationType

from config import config

class DefaultResponseType(ObjectType):
    ''' the same answer for all queries, 
        depends on frontend query '''
    __schema__ = gql( """
        type DefaultResponse{
            user_info: [Users]            
            token_info: Token
            license_info: [License]            
            order_info: [Order]           
            notification_info: [Notification]            
            message: String
            status: Int
            error: String            
            next: Int
            previous: Int
            count: Int
        }
    """
    )
    __requires__ = [UserType, TokenType, OrderType, LicenseType, NotificationType]

class Query(ObjectType):
    ''' main class query
            all existing queries (input parameters): response to frontend(DefaultResponseType)'''
    __schema__ = gql( """
        type Query {
            loginUser( login_user: String!, login_password: String!): DefaultResponse
            getUser( status: ItemStatus, user_id: Int, page: Int, limit: Int): DefaultResponse  
            getLicense( status:  ItemStatus, user_id: Int, license_id: Int, page: Int, limit: Int): DefaultResponse      
            getOrder( form_id: String, order_id: Int, page: Int, limit: Int): DefaultResponse
            getUrls( user_id: Int, order_id: Int, page: Int, limit: Int): DefaultResponse
            getNotification( user_id: String, seen: Boolean, page: Int, limit: Int): DefaultResponse        
        }
    """
    )
    __requires__ = [ItemStatusEnum, DefaultResponseType]

    @staticmethod
    async def resolve_loginUser(_, info, **data):
        ''' connect the query with user microservices and active jaeger tracer
        require:
            info: request data
            data: info user and password to login'''       
        try:
            c=await ResolverRequest( data=data, 
                    url=f"{config['IP_USERS']}/login/", 
                    headers=info.context['headers_token'],
                    method='POST', 
                ).resolve_default(jaeger='loginUserQuery',
                    context=info.context, notification_type=''
                )
            print(' -C: ')
            return c
        except:
            return get_error('resolve_loginUser, query',sys.exc_info())
    
    @staticmethod
    async def resolve_getUser(_, info, **data):
        ''' connect the query with user microservices, active jaeger tracer and get redis info
        require:
            info: request data
            data: info user and password to login'''       
        try:
            user_id=str(data['user_id'])+'/' if 'user_id' in data else ''
            return await ResolverRequest(
                    data=data, 
                    url=f"{config['IP_USERS']}/users/{user_id}?",
                    headers=info.context['headers_token'],
                ). resolve_default(jaeger='getUserQuery',
                    context=info.context, notification_type=''
                )
        except:
            return get_error('resolve_users, query',sys.exc_info())

    @staticmethod
    async def resolve_getLicense(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            license_id=f'/?license_id={data['license_id']}' if 'license_id' in data else '/?'
            return await ResolverRequest(
                    data=data, jaeger='getUserQuery',
                    context=info.context, url=f"{config['IP_LICENSES']}{license_id}",
                    method='POST'
                ). resolve_default()
        except:
            return get_error('resolve_getLicense, query',sys.exc_info())

    @staticmethod
    async def resolve_getOrder(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            order_id=f'/?order_id={data['order_id']}' if 'order_id' in data else '/?'
            return await ResolverRequest(
                    data=data, jaeger='getOrderQuery',
                    context=info.context, url=f"{config['IP_ORDERS']}{order_id}",
                    method='POST'
                ). resolve_default()
        except:
            return get_error('resolve_getOrder, query',sys.exc_info())

    @staticmethod
    async def resolve_getNotification(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            return await ResolverRequest(
                    data=data, jaeger='getNotificationQuery',
                    context=info.context, url=f"{config['IP_ORDERS']}/?",
                    method='POST'
                ). resolve_default()
        except:
            return get_error('resolve_getNotification, query',sys.exc_info())
