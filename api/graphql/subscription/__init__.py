'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''

import json
# Subscriptions cannot be started with ObjectType as in query or mutation. SubscriptionType should be used
from ariadne_graphql_modules  import SubscriptionType
from api.graphql.query.notification import NotificationType

from broadcaster import Broadcast

pubsub = Broadcast("memory://")

class Subscription(SubscriptionType):        
    __schema__ = """
        type Subscription {              
            updateNotifications(page: Int, limit: Int): Notification
        }
    """    
# Create QueryType instance for Query type defined in our schema...    
    __requires__ = [NotificationType]

    @staticmethod    
    async def subscribe_updateNotifications(_, info):
        async with pubsub.subscribe(channel="notification_room") as subscriber:
            async for event in subscriber:
                message = json.loads(event.message)
                yield message

    @staticmethod
    def resolve_updateNotifications(event, info):   
        return event
