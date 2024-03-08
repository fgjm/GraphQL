'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: GraphQL routes
'''
from api import app, graphql


#Routes to queries and mutations
app.mount("/graphql/", graphql)

#Route to subscriptions
app.add_websocket_route("/graphql/", graphql)
