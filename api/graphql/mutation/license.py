''' input to save license info '''

from ariadne_graphql_modules  import InputType


class LicenseCreateInput(InputType):
    __schema__ = """
    input LicenseInput {
        LicenseName: String
        capacityOrders: Int
        capacityUsers: Int           
        pesosCol: Int
        userOwner: ID
    }
    """
