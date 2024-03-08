import sys
import json
from broadcaster import Broadcast
from .send_REST import send_request

pubsub = Broadcast("memory://")


async def create_notification(data, type_notification ):
    ''' data loader permite guradar informacion asyncrona en info context'''
    try:
        notification={
            "userId": data["userId"],
            "type_notification": type_notification,
            "userFullName": data["userFullName"],
        }
        created_notification= await send_request({
            "method":"POST",
            "url":"http://127.0.0.1:5003", 
            "json":notification,
            "files":""
        })   
        if created_notification['status']<400:
            await pubsub.publish(channel="notification_room", message=json.dumps(created_notification))
    except:
        print(' -create_notification',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
    return False
