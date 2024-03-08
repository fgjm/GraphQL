'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Errors 500
'''
from logs.routes import do_log


def get_error(point,error):
    """ log and response error handling 500, provided by sys.exc_info()
        Required attributes:
            point (String): endpoint, resolve (function or class)
            error(object): data error sys.exc_info
        Return: 
            response: dict to graphql frontend
    """
    do_log(str(error),point,
            error[2].tb_lineno
            ,'error')
    return {
            "status":500,
            "message": 'internal_error',
            "error": f'Point: {point}, Error: {str(error)}'
        }
