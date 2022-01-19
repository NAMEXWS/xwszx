import json

import jmespath
import requests


class BaseApi:
    def __init__(self):
        self.header = {"Content-Type": "application/json;charset=UTF-8", "Authorization": self.get_token()}

    def send(self, data):
        """请求框架"""
        a = requests.request(**data)
        print(json.dumps(a.json(), indent=2, ensure_ascii=False))
        return a

    def get_token(self):
        """获取token"""
        data = {'method': 'post',
                'url': 'http://123.56.138.96:3012/api/ainews-user/user/login',
                'headers': {"Content-Type": "application/json;charset=UTF-8"},
                'json': {"name": "lsj1", "password": "123123"}}

        return self.send(data).json().get("access_token")

    def get_id(self):
        """获取id"""
        data = {'method': 'get',
                'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group?',
                'headers': self.header,
                'params': {'page': 1, 'per_page': 10, 'start_time': '2021-12-30', 'end_time': '2022-01-13'}}
        # a = {'page': 1, 'per_page': 10, 'start_time': '2021-12-30', 'end_time': '2022-01-13'}
        # id = requests.request(method='get',
        #                       url='http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group?',
        #                       headers={"Content-Type": "application/json;charset=UTF-8",
        #                                "Authorization": self.get_token()},
        #                       params=a)
        a = jmespath.search("[?name=='学习针头痛'].id", self.send(data).json())
        return a
if __name__ == '__main__':
    a=BaseApi()
    print(a.get_id())