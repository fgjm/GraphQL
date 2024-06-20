'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''
import sys
#If MutationType is used, one mutation must be placed per class
from ariadne_graphql_modules  import ObjectType, gql
from ariadne import QueryType

from api.resolvers import ResolverRequest
from api.resolvers.request import queed_files
from api.graphql.query import DefaultResponseType
from api.graphql.query.upload import FileType, Upload
from api.graphql.mutation.user import UserCreateInput
from api.graphql.mutation.license import LicenseCreateInput
from api.graphql.mutation.order import OrderCreateInput


from logs import get_error
from config import config

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
            return await ResolverRequest(
                    data=data, jaeger='createUsersMutation',
                    context=info.context, url=f"{config['IP_USERS']}/user/",
                    method='POST'
                ). resolve_default()
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
            return await ResolverRequest(
                    data=data, jaeger='createLicensesMutation',
                    context=info.context, url=f"{config['IP_LICENSES']}",
                    method='POST'
                ). resolve_default()
        except:
            return get_error('resolve_licenses, mutation',sys.exc_info())
    
    @staticmethod
    async def resolve_createOrders(_, info, **data):   
        ''' send data order to save in microservice 5003
            Load new order in cache
            create notification'''
        try:
            return await ResolverRequest(
                    data=data, jaeger='createOrdersMutation',
                    context=info.context, url=f"{config['IP_ORDERS']}",
                    method='POST'
                ).resolve_default()
        except:
            return get_error('resolve_orders, mutation',sys.exc_info())
    
    @staticmethod
    async def resolve_uploadFiles(_, info, files, orderInfo):
        try:           
            created_file= {
                "method":"POST",
                "url":"http://127.0.0.1:5004", 
                "json": orderInfo,
                'files': files,
                'headers':info.context['headers_token']
            }
            queed_files.append(created_file)            
            return {
                "status":201,
                "message": 'processing_files'
            }
        except:
            return get_error('uploadFiles, mutation',sys.exc_info())
