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
from api.resolvers import send_request
# detect error 500
from logs import get_error

# Load all query schemas
from .user import UserType, ItemStatusEnum, TokenType
from .search import SearchType
from .order import OrderType
from .license import LicenseType
from .notification import NotificationType

#recurring query caching library
from aiodataloader import DataLoader
#Call all dataloaders
from api.resolvers.data_loader import *

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
    ''' main class query'''
    __schema__ = gql( """
        type Query {
            loginUser( login_user: String !, login_password: String!): DefaultResponse
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
        ''' connect the query with user microservices
        require:
            info: request data
            data: info user and password to login'''       
        try:
            #load to api.info_context.py
            user_token= info.context['user_token']
            query= info.context['query']
            #Get redis data if redis id exits
            response_cache = await get_users_redis(user_token,query)
            if response_cache:
                print('response_cache:',response_cache)
                return response_cache
            res = await send_request({                
                "url":"http://127.0.0.1:5001/login/",
                "method":"POST",
                "json":data,
                'headers': info.context['headers_token']
            })    
            print('res:', res)                
            return res
        except:
            return get_error('resolve_loginUser, query',sys.exc_info())
    
    @staticmethod
    async def resolve_getUser(_, info, **data):
        '''info: object specific for this field and query'''
        try:           
            page=data['page'] if 'page' in data else 1
            limit=data['limit'] if 'limit' in data else 5
            user_id=str(data['user_id'])+'/' if 'user_id' in data else ''
            #response_cache= await info.context['data_loader']
            user_token= info.context['user_token']
            query= info.context['query']
            response_cache = await get_users_redis(user_token,query)
            if response_cache:
                return response_cache
            res = await send_request({                
                "url":f"http://127.0.0.1:5001/users/{user_id}?page={page}&limit={limit}", 
                "json":data,
                'headers': info.context['headers_token']
            }) 
            await set_users_redis(user_token,query, res)
            return res
        except:
            return get_error('resolve_users, query',sys.exc_info())

    @staticmethod
    async def resolve_getLicense(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            license_id=data['license_id'] if 'license_id' in data else -1
            user_owner=data['user_id'] if 'user_id' in data else -1  
            response_cache= await info.context['license_loader'].load(1)    
            if response_cache:
                return response_cache  
            res= await send_request({                
                "url":f"http://127.0.0.1:5002/license/?license_id={license_id}&user_owner={user_owner}", 
                "json":data,
                'headers': info.context['headers_token']
            })
            print('License:',f"http://127.0.0.1:5002/license/?license_id={license_id}&user_owner={user_owner}", res)           
            return res   
        except:
            return get_error('resolve_getLicense, query',sys.exc_info())

    @staticmethod
    async def resolve_getOrder(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            response_cache= await info.context['order_loader'].load()    
            if response_cache:
                return response_cache            
            return send_request({                
                "url":"http://127.0.0.1:5003", 
                "json":data
            })            
        except:
            return get_error('resolve_getOrder, query',sys.exc_info())

    @staticmethod
    async def resolve_getNotification(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            response_cache= await info.context['notification_loader'].load()    
            if response_cache:
                return response_cache            
            return send_request({                
                "url":"http://127.0.0.1:5005", 
                "json":data
            })            
        except:
            return get_error('resolve_getNotification, query',sys.exc_info())
