'''
    @author: Giovanni Junco
    @since: 01-03-2024
    @summary: All tests
'''

from main import app
from starlette.testclient import TestClient
from .queries_users import query_user

TOKEN='Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA5ODgwMTAwLCJpYXQiOjE3MDk4NDAxMDAsImp0aSI6ImM5ZGFmMGU2ZWU0NjRlNDM4NjNlZjYzNTM5Y2FiMWE5IiwidXNlcl9pZCI6MX0.pkXSWQtF94xmKDKuJAc94clz_DGenWq5qmRNvNGJeg0'

def test_playground():
    ''' Returns OK if test status is 200, load playground ariadne graphql'''
    client = TestClient(app)
    response = client.get('/graphql/')
    assert response.status_code == 200

def test_get_users():
    ''' Returns OK if test status is 200, return all user info'''
    QUERY_NAME='getUser'
    QUERY={'variables': {'page': 1, 'limit': 10},'query':query_user[QUERY_NAME]['QUERY']}
    client = TestClient(app)
    client.headers = {"Authorization": TOKEN}
    response = client.post('/graphql/', json=QUERY)
    assert response.status_code == 200
