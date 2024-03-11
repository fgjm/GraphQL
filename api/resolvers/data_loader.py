'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Info to data loaders - redis
'''
#get internal error info
import sys
#get redis data
from .redis import RedisClass

def make_redis_id(user_id,query):
    return f'USER_*{user_id}{query}'

async def get_users_redis(user_id,query):
    ''' Get query user save in redis'''
    try:     
        redis_id=make_redis_id(user_id,query)           
        response=RedisClass( redis_id ).get()
        return response if response else ''
    except:
        print(' -get_users_redis, dataloader.py',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return ''

async def set_users_redis(user_id,query, data):
    ''' Get query user save in redis'''
    try:
        if data['status'] <400:
            redis_id=make_redis_id(user_id,query)
            return RedisClass(redis_id).set(data)
    except:
        print(' -get_users_redis, dataloader.py',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
    return False

