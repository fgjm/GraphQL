import sys
from starlette.responses import PlainTextResponse

async def file_update(request):
    try:
        async with request.form() as form:
            if "upload_file" in form:
                filename = form["upload_file"].filename
                print(filename, form["upload_file"].file)
                contents = form["upload_file"].file.read()
                with open(filename, "wb") as buffer:
                    buffer.write(contents)
                    buffer.close()
                return PlainTextResponse('File save')
        return PlainTextResponse('File dont save')
    except:
        print(' -file_update',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return PlainTextResponse('Error')