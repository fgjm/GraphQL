

def on_connect(websocket, params):
    print(' on_connect:',websocket.scope, params)
    if not isinstance(params, dict):
        websocket.scope["connection_params"] = {}
        return

    # websocket.scope is a dict acting as a "bag"
    # stores data for the duration of connection
    websocket.scope["connection_params"] = {
        "token": params.get("token"),
    }

def on_disconnect(websocket):
    print('on_disconnect:',websocket.scope)
    """ chat_user = websocket.scope.get("chat_user")
    if chat_user:
        chat_user.set_offline() """
