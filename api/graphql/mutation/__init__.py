''' si se usa MutationType se debe colocar una mutacion por clase '''
import sys
from ariadne_graphql_modules  import ObjectType, gql
from ariadne import QueryType

from api.resolvers import send_request
from api.graphql.query import DefaultResponseType
from api.graphql.query.upload import FileType, Upload
from api.graphql.mutation.user import UserCreateInput
from api.graphql.mutation.license import LicenseCreateInput
from api.graphql.mutation.order import OrderCreateInput

from api.graphql.cache import load_cache
from api.graphql.mutation.uploadFile import queed_files
from .notification import list_notification
from logs import get_error

class Mutation(ObjectType):        
    __schema__ = gql( """
        type Mutation {
            createUsers(user_data: UserInput!): DefaultResponse
            updateUsers(user_data: UserInput!, user_id:Int): DefaultResponse
            removeUsers(user_id:Int): DefaultResponse
            
            createLicenses(license_data: LicenseInput): DefaultResponse
            updateLicenses(license_data: LicenseInput, license_id: Int): DefaultResponse
            removeLicenses(license_id: Int): DefaultResponse
            
            createOrders(order_data: OrderInput): DefaultResponse
            updateOrders(order_data: OrderInput, order_id: Int): DefaultResponse
            removeOrders(order_id: Int): DefaultResponse
            
            uploadFiles(files: [Upload!]!, order_data: OrderInput): [uploadedFiles]
        }
    """
    )
    __requires__ = [  DefaultResponseType, UserCreateInput, LicenseCreateInput,OrderCreateInput, FileType, Upload]

    @staticmethod
    async def resolve_createUsers(_, info, **data):   
        ''' send data user to save in microservice 5001
            Load new user in cache
            create notification to user'''
        try:
            created_user= send_request({
                "method":"POST",
                "url":"http://127.0.0.1:5001", 
                "json":data
            })
            if created_user['status']<400:
                load_cache(info, created_user, 'user_loader')
                list_notification.append(('user_loader', created_user['id']))
            return created_user
        except:
            return get_error('resolve_users, mutation',sys.exc_info())
        
    query_type = QueryType()

    @query_type.field("random")
    @staticmethod
    async def resolve_createLicenses(_, info, **data):   
        ''' send data license to save in microservice 5002
            Load new license in cache
        '''
        try:
            created_licenses= send_request({
                "method":"POST",
                "url":"http://127.0.0.1:5002", 
                "json":data
            })
            if created_licenses['status']<400:
                load_cache(info, created_licenses, 'licenses_loader')                
            return created_licenses
        except:
            return get_error('resolve_licenses, mutation',sys.exc_info())
    
    @staticmethod
    async def resolve_createOrders(_, info, **data):   
        ''' send data order to save in microservice 5003
            Load new order in cache
            create notification'''
        try:
            created_order= send_request({
                "method":"POST",
                "url":"http://127.0.0.1:5003", 
                "json":data
            })
            if created_order['status']<400:
                load_cache(info, created_order, 'order_loader')
                list_notification.append(('order_loader', created_order['id']))
            return created_order
        except:
            return get_error('resolve_orders, mutation',sys.exc_info())
    
    @staticmethod
    async def resolve_uploadFiles(*_, files, orderInfo):
        try:           
            created_file= {
                "method":"POST",
                "url":"http://127.0.0.1:5004", 
                "json": orderInfo,
                'files': files
            }
            queed_files.append(created_file)            
            return {
                "status":200,
                "message": 'Transaction completed',
            }
        except:
            return get_error('uploadFiles, mutation',sys.exc_info())
