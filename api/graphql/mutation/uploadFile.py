''' notification creation '''
import sys
from api.utilities import get_error
from api.resolvers import send_request
from logs.routes import do_log

queed_files = []

async def send_queed_files():
    ''' Organizes the information to save the notification in the microservice 5005
        Clear pending notifications'''
    try:
        for file in queed_files:            
            saved_file= send_request(file)
            if saved_file['status']<400:
                queed_files.remove(file)
                continue
            do_log('Error to upload file',saved_file['error'],
                    saved_file['status'] ,'error')
    except:
        get_error('send_queed_files, uploadFile.py',sys.exc_info())
