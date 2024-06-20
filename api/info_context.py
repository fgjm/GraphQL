'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Load app GraphQL Ariadne
'''
#call token to user id
from .resolvers.token_decode import get_token_user_id
#call log
from logs import do_log

async def get_context_value(request, data):
    ''' Get all the data from the request and set DataLoaders
        Note: 
            - data loader: allows saving asynchronous information in info context
            - if you do not want to use cachinge: DataLoader(get_users_from_api, cache=False)'''
    #log user queries
    query_name= data.get("operationName", "No_name") 
    query_variables= data.get("variables", "No_variables")    
    do_log('', f'{query_name} - {query_variables}', 'Graphql','info')
    #Get user id from token to look or save in redis
    not_use_token=['LoginUser']
    user= get_token_user_id(request.headers) if query_name not in not_use_token else ''
    #Get query to redis id
    query= data.get("query", "mutation") 
    #get token to send
    token = request.headers.get("Authorization", "No_token") 
    return {
        "request":request,
        'user_token':user,
        'query': '' if 'mutation' in query else query,
        'headers_token': token
    }