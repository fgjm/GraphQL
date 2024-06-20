'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''
import sys
from asgi_background import BackgroundTasks
from logs import get_error
from .redis import RedisClass

import json
from broadcaster import Broadcast
from .request import ResolverRequest, queed_redis, queed_notification, queed_files
from config import config
from logs import get_error

pubsub = Broadcast("memory://")


class tasks_background():

    async def create_notification(self):
        ''' save notification in microservice 5004, and send by socket connection'''
        try:
            for notification in queed_notification:
                created_notification= await ResolverRequest(
                            data=notification,
                            url=f"{config['IP_NOTIFICATIONS']}",
                            method='POST'
                        ). send_request()   
                if created_notification['status']<400:
                    queed_notification.remove(notification)
                    await pubsub.publish(channel="notification_room", message=json.dumps(created_notification))
        except:
            get_error('create_notification, resolvers - background',sys.exc_info())
    
    async def set_users_redis(self):
        ''' Get query user save in redis'''
        try:
            for redis_data in queed_redis:
                redis_result=RedisClass(redis_data['user_token'],redis_data['query']).set(redis_data['data'])
                if redis_result:
                    queed_redis.remove(redis_data)
        except:
            get_error('set_users_redis, resolvers - background',sys.exc_info())
    
    async def send_queed_files(self):
        ''' Organizes the information to save the notification in the microservice 5005
            Clear pending notifications'''
        try:
            for file in queed_files:            
                saved_file= await ResolverRequest(
                        data=file['json'], headers=file['headers'],
                        url=f"{config['IP_UPLOAD_FILES']}",
                        method='POST', files=file['files']
                    ). send_request()  
                if saved_file['status']<400:
                    queed_files.remove(file)
                    continue
        except:
            get_error('send_queed_files, resolvers - background',sys.exc_info())

    async def exec(self, scope):
        ''' connect the queries with user microservices'''       
        try:
            tasks = BackgroundTasks(scope)
            await tasks.add_task(self.set_users_redis)
            await tasks.add_task(self.create_notification)
            return True
        except:
            get_error('resolve_default, query',sys.exc_info())
