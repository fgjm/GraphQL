''' CURD cache grapgql - context'''
import sys

from api.utilities import get_error

def load_cache(info,data,service):
    try:
        info.context[service].prime(data['id'], data)
    except:
        get_error('load_cache, store.py',sys.exc_info())

def clear_cache(info,data,service):
    ''' Delete data in info context - clear cache'''
    try:
        #info.context['user_loader'].clear(4)
        info.context["user_loader"].clear_all()
    except:
        get_error('load_cache, store.py',sys.exc_info())

def update_cache(info,data,service):
    try:
        #info.context['user_loader'].clear(4)
        info.context["user_loader"].clear_all()
    except:
        get_error('load_cache, store.py',sys.exc_info())

def get_cache(info,data,service):
    try:
        #info.context['user_loader'].clear(4)
        info.context["user_loader"].clear_all()
    except:
        get_error('load_cache, store.py',sys.exc_info())