''' notification creation '''
import sys
from logs import get_error
from api.resolvers import send_request
from logs import do_log

list_notification = []

async def create_notification(info):
    ''' Organizes the information to save the notification in the microservice 5005
        Clear pending notifications'''
    try:
        for content in list_notification:
            res= await info.context[content[0]].load(content[1])
            notification={ "content": res, "type_action": content[0]}
            created_notification= send_request({
                "method":"POST",
                "url":"http://127.0.0.1:5005", 
                "json":notification,
                "files":""
            })
            if created_notification['status']<400:
                list_notification.remove(content)
                continue
            do_log('Error to create notification',created_notification['error'],
                created_notification['status'] ,'error')
    except:
        get_error('load_cache, store.py',sys.exc_info())