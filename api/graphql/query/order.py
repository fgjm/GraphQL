''' reading data '''

from ariadne_graphql_modules  import ObjectType, gql
from .search import SearchType
from .Forms import FormsType
from .user import UserType

class OrderDataType(ObjectType):        
    __schema__ = gql( """
        type OrderData implements SearchResult {
            BusinessName: String
            Nit: String
            LegalRepresentative: String
            OfficeAddress: String
            City: String
            WebSite: String
            Mail: String
            Phone: Int
            TaxableYear: String
        }               
    """
    )
    __requires__ = [ SearchType]

class AuditTeamType(ObjectType):        
    __schema__ = gql( """
        type AuditTeam {
            Partner: String
            AuditManager: String
            AuditorCharge1: String
            AuditorCharge2: String
        }               
    """
    )

class OrderType(ObjectType):        
    __schema__ = gql( """
        type Order {            
            userOwner: Users
            orderLicense: String            
            OrderData: OrderData
            AuditTeam: AuditTeam            
            Forms: Forms
            
            createdAt: String
            modificated: String
        }               
    """
    )
    __requires__ = [OrderDataType, AuditTeamType, FormsType, UserType]
