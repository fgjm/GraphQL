'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''

from ariadne_graphql_modules  import ObjectType, gql

class NotificationType(ObjectType):        
    __schema__ = gql( """
        type Notification{      
            id: ID           
            type_action: String
            seen: Boolean
            text: String
            
            createdAt: String
            modificated: String            
        }
    """
    )
