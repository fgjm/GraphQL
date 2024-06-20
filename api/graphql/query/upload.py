'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''

from ariadne_graphql_modules  import ObjectType, ScalarType, gql


class FileType(ObjectType):        
    __schema__ = gql( """
        type uploadedFiles{
            id: ID
            url: String
            orderFormId: ID            
            formCategoryId: ID
            
            createdAt: String
            modificated: String
        }
    """
    )

class Upload(ScalarType):        
    __schema__ = """ scalar Upload """
