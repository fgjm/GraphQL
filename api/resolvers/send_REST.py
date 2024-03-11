import sys
import json
import http.client
from httpx import AsyncClient, Request
from logs import get_error


def validate_error(response):
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
    
async def send_request(data):
    ''' data loader permite guradar informacion asyncrona en info context'''
    try:
        request = Request(
            method=data['method'] if 'method' in data else 'GET',
            url=data['url'], 
            json=data['json']  if 'json' in data else '',
            files=data['files'] if 'files' in data else '',
            #headers=data['headers'] if 'headers' in data else ''
            headers={'Authorization': data['headers']}
        )        
        async with AsyncClient() as client:
            response =  await client.send(request)
            return validate_error(response)
    except:
        return get_error('send_request, REST',sys.exc_info())
        
