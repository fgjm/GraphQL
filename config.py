'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Core environment variables
'''
import os
from dotenv import load_dotenv

# Get path for .env file
ENV = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(ENV):
    # Load the data in .env
    load_dotenv(ENV)


development_config={
    'DEBUG' : True,
    "SECRET_KEY": os.getenv('SECRET_KEY'),
    "IP_REDIS": os.getenv('IP_REDIS'),
    "PORT_REDIS": os.getenv('PORT_REDIS'),

    "IP_USERS": os.getenv('IP_USERS'),
    "IP_LICENSES": os.getenv('IP_LICENSES'),
    "IP_ORDERS": os.getenv('IP_ORDERS'),
    "IP_UPLOAD_FILES": os.getenv('IP_UPLOAD_FILES'),
    "IP_NOTIFICATIONS": os.getenv('IP_NOTIFICATIONS'),
}
testing_config={
    'DEBUG' : True,
    'SECRET_KEY'  : os.getenv('SECRET_KEY')
}

production_config={
    'DEBUG' : False,
    'SECRET_KEY'  : os.getenv('SECRET_KEY')
}

all_config={
    'development': development_config,
    'testing': testing_config,
    'production': production_config
}
config=all_config[os.getenv('ENVIRONMENT')]