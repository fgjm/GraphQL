'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: socket events
'''

def on_connect(websocket, params):
    ''' If the connection is established, the user token is loaded as a connection parameter
        Required attributes:
            websocket: Subscription connection protocol
            params: metadata connection
        Return: 
            empty '''
    #print(' on_connect:',websocket.scope, params)
    if not isinstance(params, dict):
        websocket.scope["connection_params"] = {}
        return
    # websocket.scope is a dict acting as a "bag"
    # stores data for the duration of connection
    websocket.scope["connection_params"] = {
        "token": params.get("token"),
    }

def on_disconnect(websocket):
    ''' If the connection is disconnected, the status connection change to offline
        Required attributes:
            websocket: Subscription connection protocol
            params: metadata connection
        Return: 
            empty '''
    #print('on_disconnect:',websocket.scope)
    chat_user = websocket.scope.get("chat_user")
    if chat_user:
        chat_user.set_offline()
