'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''
import sys
import json
import http.client
from httpx import AsyncClient, Request

from logs import get_error
#Call Jaeger tracer
from .jaeger import tracer

from .redis import RedisClass

queed_redis = []
queed_notification = []
queed_files = []

class ResolverRequest:

    def __init__(self,  data, url, headers,method='GET', files='') -> None:
        self.data=data
        self.url=url
        self.headers=headers
        self.method=method
        self.files=files

    def validate_error(self,response):
        try:
            response_json=json.loads(response.text)
            response_json['status']=response.status_code
            if 'message' not in response_json:
                error='' if response.status_code <400 else 'internal_error'
                if 'detail' in response_json:
                    error=response_json['detail']
                response_json['message']=http.client.responses[response.status_code].lower().replace(' ','_')
                response_json['error']=error                
            return response_json
        except:
            return get_error('validate_error, REST',sys.exc_info())
        
    async def send_request(self):
        ''' data loader permite guradar informacion asyncrona en info context'''
        try:
            request = Request(
                method=self.method,
                url=self.url, 
                json=self.data,
                files=self.files,
                headers={'Authorization': self.headers}
            )        
            async with AsyncClient() as client:
                response =  await client.send(request)
                return self.validate_error(response)
        except:
            return get_error('send_request, REST',sys.exc_info())
    
    def load_get_parameters(self,data):
        url=f'user_owner={data['user_owner']}' if 'user_owner' in data else '' 
        url=url+f'&page={data['page']}' if 'page' in data else url
        url=url+f'&limit={data['limit']}' if 'limit' in data else url
        return url
    
    async def resolve_default(self,jaeger,context,notification_type=''):
        ''' connect the queries with user microservices
        require:
            jaeger: monitor identifier
            context: consulting user, frontend's query
            data: info user and password to login
            url: microservice address
            method: GET or POST
        return:
            response microservice    
        '''       
        try:
            #add requets to Jaeger
            with tracer.start_as_current_span(jaeger):
                pass            
            #Get redis data if redis id exits            
            response_cache = RedisClass(context['user_token'],context['query']).get() if context['user_token'] else False
            if response_cache:
                print('response_cache:',response_cache)
                return response_cache
            #url parameters
            self.url = self.url+self.load_get_parameters(self.data) if self.method=='GET' else self.url
            #http async request
            microservice_response = await self.send_request()    
            if microservice_response['status']<400 and context['user_token']:
                queed_redis.append({
                    "user_token": context['user_token'],
                    "query": context['query'], "data": microservice_response
                    })
                print('BACKG',len(queed_redis))
                
                if notification_type:
                    queed_notification.append({
                            "user_owner": self.data["userOwner"],
                            "notification_type": notification_type,
                            "user_full_name": self.data["userFullName"],
                            "headers": self.headers
                    })
            #print('res:', res)                
            return microservice_response
        except:
            return get_error('resolve_default, query',sys.exc_info())
