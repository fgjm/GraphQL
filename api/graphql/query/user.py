''' query to get user info '''

from ariadne_graphql_modules  import ObjectType, gql, EnumType


class TokenType(ObjectType):        
    __schema__ = gql( """
        type Token{
            access_token: String
            refresh_token: String        
        }
    """
    )

class UserType(ObjectType):        
    __schema__ = gql( """
        type Users{
            id: ID
            email: String
            userFullName: String
            username: String            
            userIdentification: Int
            userProfessionalCard: String
            userPhone: Int
            userPermissions: String
            userLicenses: String
            userOrders: String
            userOwner: ID
            hash: String
            createdAt: String
            modificated: String            
        }
    """
    )

class ItemStatusEnum(EnumType):        
    __schema__ = gql( """
        enum ItemStatus{
            ACTIVE
            INACTIVE
            BANNED
        }
    """
    )
