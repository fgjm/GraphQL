'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Token validation - User ID
'''
# get error system info - library
import sys
# JSON Web Tokens - library
import jwt
#get .env variables
from config import config
#call log
from logs import get_error


def get_token_user_id(headers=''):
    """ If the token is correct, it returns the ID of the logged in user
        Required attributes:
            Authorization: token (str), Bearer <token> in headers
        Return: 
            response: user_id"""
    try:
        #Get token string
        token = headers["Authorization"].split(" ")[1] if "Authorization" in headers else None
        #decode token
        data=jwt.decode(token, config['SECRET_KEY'], algorithms=["HS256"]) if token else ''
        if 'user_id' in data:
            #response user id
            return data['user_id']
        return {
                "message": "Unauthorized",
                "error": "Authentication Token is missing or user id is not valid"
            }
    except:
        return get_error('Token decode',sys.exc_info())    
