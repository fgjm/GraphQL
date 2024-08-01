
# GrahpQL

Flexible and efficient requests. GraphQL - Ariadne. Frontend Backend Connection. Improve response time.

Queries, Mutations and Asynchronous Subscriptions to organize data. Optimize independent requests from your API. Detailed information through scalable diagrams and modules. 

![Playground](/home.png)

## General diagram
![general diagram](/diagrama.png)

## Specific diagram
![specific diagram](graphql.png)

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file (root folder)

`ENVIRONMENT`
`SECRET_KEY`

`IP_REDIS`
`PORT_REDIS`

`IP_USERS`
`IP_LICENSES`
`IP_ORDERS`
`IP_UPLOAD_FILES`
`IP_NOTIFICATIONS`

## Installation

Install project with python and virtualenv

Linux
```bash
  virtualenv .venv
  source .venv/bin/activate
  pip3 install -r requirements.txt
  uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

Windows
```bash
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  uvicorn main:app --host 0.0.0.0 --port 5000 --reload
```

## Redis

Redis (Remote Dictionary Server) is an open source NoSQL in-memory data store primarily used as an application cache or database

### Ubuntu install 

https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/

```bash

curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis

sudo service redis-server start
redis-cli 
ping
PONG
```

### Windows install 

[Releases · microsoftarchive/redis (github.com)](https://github.com/microsoftarchive/redis/releases)
Download and unzip Redis-x64-3.0.504.zip
Place an environment variable path path where it is unzipped

```bash
Strat redis on windows cmd: redis-server

Get data: redis-cli  get Gioabcd123

Clear:  flushall  or flushall async

Get all: todo scan 0
```

## Playground

Ariadne brings built-in Playground to test queries and documenting schema

Starlette route link: http://127.0.0.1:5000/graphql/

![Playground](/playground.png)

## Docker

### Basic

**Python (require dockerfile in root folder):** 
```bash
docker build -t graphql:v1 .
```

**Redis:**
```bash
docker pull redis
docker run --name some-redis -p 6379:6379 -d redis
```


### Docker compose

**Start (require docker-compose.yml in root folder):** 
```bash
docker compose up
```

**Delete:**	
```bash
docker compose down
```


## Optimization (refactoring and quality standards)

The code quality and scalability depends largely on good development practices such as:
- Unit tests in different cases of operations and possible responses of microservices.
- Code debugging using the 5 Solid principles
- PyLint standards in each of the .py files

### Unittest

Require tets folder with all test queries and mutation files

pytest ./test/__init__.py

### Pylint one file

```bash
pip install pylint
python -m pylint .\app.py
```

### Pylint multiple file

pip install pylint-runner

Exec in root folder: 
pylint_runner

## Monitoring

**End-to-end distributed tracing.** Control of systems based on microservices, ease of analyzing the behavior of an application and thus solving possible errors or problems

### Jaeger

Docker: Getting Started — Jaeger documentation (jaegertracing.io)
```bash
docker run --rm --name jaeger   -e COLLECTOR_ZIPKIN_HOST_PORT=:9411   -p 6831:6831/udp   -p 6832:6832/udp   -p 5778:5778   -p 16686:16686   -p 4317:4317   -p 4318:4318   -p 14250:14250   -p 14268:14268   -p 14269:14269   -p 9411:9411   jaegertracing/all-in-one:1.51
```

http://192.168.1.127:16686/

![jaeger](Jaeger_GraphQL.png)

## Security

### Token

Set of random characters used to validate user instead of sending username and password

JWT: (json web token) encapsulate and share claims (request features).
 - have digital signature: RFC 7515 - can be generated with symmetric or asymmetric keys
 - encrypted data: contains sensitive data (do not set passwords)

[parts of a token (jwt.io)](jwt.io)




## Tech Stack

https://ariadnegraphql.org/

https://www.starlette.io/

**Server:** Python, starlette, uvicorn, ariadne, broadcast

**Author:** Giovanni Junco

**Since:** 07-03-2024

## Additional 

### Use Ubuntu in Windows

Execute power shell as administrator:
```bash
wsl --install
```

restart windows system

  username: miubuntu

  password: dfgh1278% 

### Postman
![Postman](/postman.png)




