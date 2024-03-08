''' reading data '''
import sys
from ariadne_graphql_modules  import ObjectType, gql

from api.resolvers import send_request
from api.utilities import get_error

from .user import UserType, ItemStatusEnum, TokenType
from .search import SearchType
from .order import OrderType
from .license import LicenseType
from .notification import NotificationType

class DefaultResponseType(ObjectType):        
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
# Create QueryType instance for Query type defined in our schema...    
    __requires__ = [ItemStatusEnum, DefaultResponseType]
    
    @staticmethod
    async def resolve_loginUser(_, info, **data):
        '''info: object specific for this field and query'''       
        try:
            response_cache= await info.context['login_loader'].load(1)
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
            response_cache= await info.context['user_loader'].load(1)
            if response_cache:
                print('response_cache:',response_cache)
                return response_cache
            res = await send_request({                
                "url":f"http://127.0.0.1:5001/users/{user_id}?page={page}&limit={limit}", 
                "json":data,
                'headers': info.context['headers_token']
            }) 
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
