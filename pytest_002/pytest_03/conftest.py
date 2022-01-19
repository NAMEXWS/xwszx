# import json
#
# import jmespath
# import pytest
# import requests
#
#
# @pytest.fixture()
# def token():
#     a = {"name": "lsj1", "password": "123123"}
#     b = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/user/login',
#                          json=a)
#     return b.json().get("access_token")
#
#
# @pytest.fixture()
# def header(token):
#     headers = {"Content-Type": "application/json;charset=UTF-8",
#               "Authorization": token}
#     return headers
#
#
# @pytest.fixture()
# def id(token, header):
#     b = {'page':1,'per_page':10,'start_time':'2021-12-30','end_time':'2022-01-13'}
#     id = requests.request(method='get', url='http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group?',
#                           headers=header,
#                           params=b)
#
#
#     a=jmespath.search("[?name=='薛习针tot'].id",id.json())
#     return a
