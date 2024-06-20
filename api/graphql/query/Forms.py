'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: send requests to all microservices
'''

from ariadne_graphql_modules  import ObjectType, UnionType, gql

class StartingAreaType(ObjectType):        
    __schema__ = gql( """
        type StartingArea{
            planning: String
            execution: String
            closing: String           
        }
    """
    )

class ClosingFormType(ObjectType):        
    __schema__ = gql( """
        type ClosingForm {
            c1: String
            c2: String
            c3: String
            c4: String
            c5: String
            c6: String
            c7: String
            c8: String
            c9: String            
        }               
    """
    )

class ExecutionFormType(ObjectType):        
    __schema__ = gql( """
        type ExecutionForm {
            e11: String
            e12: String
            e13: String
            e14: String
            e15: String
            e16: String
            e17: String
            e18: String
            e21: String
            e22: String
            e23: String
            e24: String
            e25: String
            e26: String
            e27: String
            e28: String
            
            e3: String
            er1: String
            er2: String
            er3: String
            er4: String
            er5: String
        }               
    """
    )

class PlanningFormType(ObjectType):        
    __schema__ = gql( """
        type PlanningForm {
            p1: String
            p2: String
            p3: String
            p4: String
            p5: String
            p6: String
            p7: String
            p8: String
            p9: String
            p10: String
            p11: String
        }               
    """
    )


class FormsType( UnionType):        
    __schema__ = "union Forms= StartingArea | PlanningForm | ExecutionForm | ClosingForm"
    __requires__ = [StartingAreaType, PlanningFormType, ExecutionFormType, ClosingFormType]
    @staticmethod
    def resolve_type(obj, *_):
        if isinstance(obj, dict) and obj.get("__typename"):
            return obj["__typename"]
        raise ValueError(f"Don't know GraphQL type for '{obj}'!")
