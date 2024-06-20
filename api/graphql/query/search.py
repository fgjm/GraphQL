'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''

from ariadne_graphql_modules  import InterfaceType

class SearchType(InterfaceType):        
    __schema__ = """
        interface SearchResult {   
            BusinessName: String
            Nit: String
        }
    """
    
    @staticmethod
    def resolve_type(obj, *_):
        if isinstance(obj, dict) and obj.get("__typename"):
            return obj["__typename"]

        raise ValueError(f"Don't know GraphQL type for '{obj}'!")
