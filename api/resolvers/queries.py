''' reading data '''
import sys
import datetime
from bs4 import BeautifulSoup
import requests

# Create QueryType instance for Query type defined in our schema...

DOLLAR_VALUE=[datetime.datetime.utcnow().date(),0]
def get_dollar_now():
    try:
        now=datetime.datetime.utcnow().date()
        if now >= DOLLAR_VALUE[0]:
            DOLLAR_VALUE[0]=(datetime.datetime.utcnow() + datetime.timedelta(days=1)).date()
            api_url = f"https://dolar.wilkinsonpc.com.co/widgets/gratis/indicadores-economicos-min.html"
            ids_map =  requests.get(api_url)
            soup = BeautifulSoup(ids_map.text, 'html.parser')
            DOLLAR_VALUE[1]=soup.find('table' ,id='tabla-indicadores_ind_todos').find('span').text.strip()
            DOLLAR_VALUE[1]=float(DOLLAR_VALUE[1].replace('$','').replace(',','') )

        return DOLLAR_VALUE[1]
    except:
        print('Indicadores no encontrados: ',sys.exc_info(),'Line:',sys.exc_info()[2].tb_lineno)
