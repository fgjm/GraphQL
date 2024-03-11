'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: Errors handlers
'''
from starlette.responses import JSONResponse
#Internal Error Handler library
from starlette.exceptions import HTTPException
from starlette.requests import Request
#call log
from logs import do_log

async def http_exception(request: Request, exc: HTTPException):
    ''' Detects unexpected errors '''
    do_log(' Exception_handlers', f'{exc.detail} - {exc.status_code}', request.url,'error')
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)

#errors to detect
exception_handlers = {
    Exception: http_exception,
    HTTPException: http_exception,
    405: http_exception,
    500: http_exception
}