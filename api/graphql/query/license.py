''' reading data '''

from ariadne_graphql_modules  import ObjectType, ScalarType, gql, DirectiveType

from .user import UserType


from ariadne import SchemaDirectiveVisitor
from graphql import default_field_resolver


class DateDirective(SchemaDirectiveVisitor):
    def visit_field_definition(self, field, object_type):
        date_format = self.args.get("format")
        original_resolver = field.resolve or default_field_resolver

        def resolve_formatted_date(obj, info, **kwargs):
            result = original_resolver(obj, info, **kwargs)
            if result is None:
                return None

            if date_format:
                return result.strftime(date_format)

            return result.isoformat()

        field.resolve = resolve_formatted_date
        return field


class PrefixStringDirective(DirectiveType):
    __schema__ = "directive @date(format: String) on FIELD_DEFINITION"
    __visitor__ = DateDirective

class Money(ScalarType):        
    __schema__ =  """ scalar Money """

class LicenseType(ObjectType):        
    __schema__ = gql( """
        type License{
            # Union de los tres tipos de contenidos   
            orders_quantity: Int
            users_quantity: Int            
            " tipo escalar adicional contiene el valor de conversion (dolares) y tipo de moneda "
            revenue: Money
            # user info> username, imageProfile, id  
            pesos_col: Int
            user_owner: Users
            license_id: ID!
            license_name: String
            
            is_active: Boolean
            is_banned: Boolean
            
            createdAt: String @date(format: "%Y-%m-%d %H")
            modificated: String @date(format: "%Y-%m-%d %H")            
        }
    """
    )
    __requires__ = [Money, UserType, PrefixStringDirective]
    __aliases__ = {
        "license_name": "NAME"
    }
