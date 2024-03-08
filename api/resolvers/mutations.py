''' reating, updating or deleting data '''
import sys
import base64

def signupBase64(encode_file):
    try:
        """ por probar: envio de imagenes en base 64- no implementado"""
        file=encode_file.split(';base64,')
        ext=file[0].split('/')[1]
        if(ext=='mpeg'): 
            ext='mp3'
        if not ext:
            return {"msg":"The field encode_file must start with: data: media_type/extension;base64"}
        decoded_data=base64.b64decode((file[1]))
        img_file = open(f'imagePr.{ext}', 'wb')
        img_file.write(decoded_data)
        img_file.close()
        return True
    except:
        print(' error signupBase64',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return 'Error'

def save_file(files):
    try:
        print(' -multipleUpload:',files)
        for file in files:
            filename = file.filename
            print(filename)
            contents = file.file.read()
            with open(filename, "wb") as buffer:
                buffer.write(contents)
                buffer.close() 
        return True
    except:
        print(' error-multipleUpload',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
        return 'Error'
