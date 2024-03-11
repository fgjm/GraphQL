'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Core environment variables
'''
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {    
    "HOST_SQL" : os.getenv('HOST_SQL'),
    "USER_SQL" : os.getenv('USER_SQL'),
    "PWD_SQL" : os.getenv('PWD_SQL'),
    "SECRET_KEY": os.getenv('SECRET_KEY'),
    "IP_MONGODB_POST": os.getenv('IP_MONGODB_POST'),
    "IP_MONGODB_STORY": os.getenv('IP_MONGODB_STORY'),
    "IP_GLOOV_LOGIN": os.getenv('IP_GLOOV_LOGIN'),
    "IP_GRAPHQL_MARIADB": os.getenv('IP_GRAPHQL_MARIADB'),
    "IP_GRAPHQL_MONGODB": os.getenv('IP_GRAPHQL_MONGODB'),
    
    "IP_MARIADB_PROFILE": os.getenv('IP_MARIADB_PROFILE'),
    "IP_MARIADB_ARCHIVED": os.getenv('IP_MARIADB_ARCHIVED'),
    "IP_MARIADB_NOTIFICATION": os.getenv('IP_MARIADB_NOTIFICATION'),
    "IP_MARIADB_STATISTICS": os.getenv('IP_MARIADB_STATISTICS'),
    "IP_MARIADB_TRANSACTIONS": os.getenv('IP_MARIADB_TRANSACTIONS'),
    "IP_MARIADB_REPORT": os.getenv('IP_MARIADB_REPORT'),
    "IP_JELLYFIN": os.getenv('IP_JELLYFIN'),   
    "IP_CALLS": os.getenv('IP_CALLS'),
    "IP_CHAT" : os.getenv('IP_CHAT'),
    "IP_CHAT_GROUP"  : os.getenv('IP_CHAT_GROUP')
}
