'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''
import sys
import redis
import json

from config import config
from logs import get_error

redis_server = redis.Redis(host=config['IP_REDIS'],port=config['PORT_REDIS'])


class RedisClass:
    def __init__(self, id, query):
        self.id = f'USER_*{id}{query}'
    
    def clear_all(self):
        try:
            list_key_redis =list(redis_server.scan_iter('USER_*'))
            redis_size = redis_server.dbsize()
            if  len(list_key_redis) > 30 or redis_size > 10:
                redis_server.flushdb()
            return True
        except:
            get_error('clear, redis',sys.exc_info())
        return False

    def set(self, data):
        try:
            print('set redis:', self)
            self.clear_all()       
            if isinstance(data, list):
                data = '|*'.join([json.dumps(dt, indent=4, sort_keys=True, default=str) for dt in data]) 
            else:
                data = json.dumps(data, indent=4, sort_keys=True, default=str)
            redis_server.mset({self.id: data })
            return True
        except:
            get_error('set, redis',sys.exc_info())
        return False

    def get(self):
        try:   
            if redis_server.exists(self.id)!=0:                
                result_redis=redis_server.get(self.id).decode("utf-8").split('|*')                
                if len(result_redis)>1:
                    result_redis=[json.loads(data) for data in result_redis]
                else:
                    result_redis=json.loads(result_redis[0])                
                return result_redis
        except:
            get_error('get, redis',sys.exc_info())
        return False

    def delete(self):
        try:
            redis_server.delete(self.id)
            return True
        except:
            get_error('delete, redis',sys.exc_info())
        return False
