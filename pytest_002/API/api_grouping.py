import json

from pytest_002.API.base_api import BaseApi


class Grouping(BaseApi):
    def get_list(self):
        """获取分组页面信息 """
        data = {'method': "get",
                'url': "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
                'headers': {'Content-Type': 'application/json; charset=utf-8', 'Authorization': self.get_token()},
                'params': {"page": 1,
                           "per_page": 10,
                           "start_time": "2021-12-30",
                           "end_time": "2022-01-13"}}
        return self.send(data)

    def create_group(self):
        """创建分组"""
        data = {'method': 'post',
                'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/create',
                'headers': {'Content-Type': 'application/json; charset=utf-8', 'Authorization': self.get_token()},
                'json': {"name": "学习针头痛"}}
        return self.send(data)

    def add_company(self):
        """添加公司"""
        data = {'method': 'post',
                'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
                'headers': {'Content-Type': 'application/json; charset=utf-8', 'Authorization': self.get_token()},
                'json': {"company_code": "000001", "group_id": self.get_id()}}
        return self.send(data)

    def del_group(self):
        """删除分组"""
        data = {'method': 'get',
                'url': 'http://123.56.138.96:3012/api/ainews-user/company-group/delete?',
                'headers': {'Content-Type': 'application/json; charset=utf-8', 'Authorization': self.get_token()},
                'params': {"id": self.get_id()}}
        return self.send(data)
