''' input to save user info '''

from ariadne_graphql_modules  import InputType



class UserCreateInput(InputType):
    __schema__ = """
    input UserInput {
        email: String
        Password: String
        userFullName: String
        username: String
        
        userIdentification: Int
        userProfessionalCard: String
        userPhone: Int
        userPermissions: String
        userLicenses: String
        userOrders: String
        userOwner: ID
    }
    """
    __args__ = {
        "userFullName": "user_full_name",
    }