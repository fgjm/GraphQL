''' reading data '''

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
