''' input to save Order info '''

from ariadne_graphql_modules  import InputType



class OrderCreateInput(InputType):
    __schema__ = """
    input OrderInput {
        BusinessName: String
        Nit: String
        LegalRepresentative: String
        OfficeAddress: String
        City: String
        WebSite: String
        Mail: String
        Phone: Int
        TaxableYear: String
        
        Partner: String
        AuditManager: String
        AuditorCharge1: String
        AuditorCharge2: String
        userOwner: ID
    }
    """