
# Auditando.co GrahpQL

Flexible and efficient requests. GraphQL - Ariadne. Frontend Backend Connection
Queries, Mutations and Asynchronous Subscriptions to organize data. Optimize independent requests from your API. Detailed information through scalable diagrams and modules.
Improve response time


## General diagram
![general diagram](/diagrama_auditando_co.png)

## Specific diagram
![specific diagram](auditando_co_graphql.png)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file


## Installation

Install project with python and virtualenv

Linux
```bash
  virtualenv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
  uvicorn app:app --port 5000 --reload
```

Windows
```bash
  python -m venv .auditando_ariadne
  .auditando_ariadne\Scripts\activate
  pip install -r requirements.txt
  uvicorn app:app --port 5000 --reload
```
## redis

Redis (REmote DIctionary Server) es un almacén de datos NoSQL de código abierto en memoria que se utiliza principalmente como caché de aplicaciones o base 

Iniciar redis en windows cmd: redis-server

validar: redis-cli  get Gioabcd123

ver colas de celery: llen celery

clear:  flushall  or flushall async

ver todo scan 0

## Unittest

pytest ./test/__init__.py

## Pylint one file

```bash
pip install pylint
python -m pylint .\app.py
```

## Pylint multiple file

pip install pylint-runner

en la carpeta raíz
pylint_runner

## Tech Stack
https://ariadnegraphql.org/
https://www.starlette.io/
**Server:** Python, uvicorn, ariadne, broadcast


