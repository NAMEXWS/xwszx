# import json
#
# import jmespath
# import pytest
# import requests
#
#
# @pytest.fixture()
# def token():
#     RequestBody = {"name": "lsj1", "password": "123123"}
#     b = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/user/login',
#                          json=RequestBody)
#     print(json.dumps(b.json(), indent=4, ensure_ascii=False))
#     return b.json().get("access_token")
#     # print(b.json().get("access_token"))
#     # return jmespath.search('access_token',b.json())
#
#
# @pytest.fixture()
# def id(token):
#     RequestBody = {"name": "薛习针tot"}
#     c = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/company-group/create',
#                          headers={"Authorization": token},
#                          json=RequestBody)
#     print(json.dumps(c.json(), indent=4, ensure_ascii=False))
#     return c.json().get('id')


# class GSYQ:
#
#     def tianjiafenzu(self, token):
#         RequestBody = {"name": "薛习针tot"}
#         c = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/company-group/create',
#                              headers={"Authorization": token},
#                              json=RequestBody)
#         print(json.dumps(c.json(), indent=4, ensure_ascii=False))
#         # assert jmespath.search('name', c.json()) == '薛习针tot'
#
#     def tianjiagongsi(self, token, id):
#         RequestBody = {"company_code": "000001", "group_id": id}
#         d = requests.request(method='post',
#                              url='http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
#                              headers={"Authorization": token},
#                              json=RequestBody)
#         print(json.dumps(d.json(), indent=4, ensure_ascii=False))
#         # assert jmespath.search('cn_name', d.json()) != ''
#
#     def more(self, token):
#         RequestBody = {"start_time": "2022-01-04T17:22:16", "end_time": "2022-01-11T17:22:16", "page": 1,
#                        "pagesize": 20}
#
#         e = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news',
#                              headers={"Authorization": token},
#                              json=RequestBody)
#         print(json.dumps(e.json(), indent=4, ensure_ascii=False))
#         # assert jmespath.search('ok', e.json()) == True
#
#     def gongsiliebiao(self, token, id):
#         RequestBody = {"page": "1", "page_size": 10, "order_by": "", "order_type": "DESC", "cp_type": "", "board": "",
#                        "keyword": "", "is_new_data": 0, "classification": "", "category_key": "", "min_score": 0,
#                        "max_score": 100, "start_time": "2021-12-28", "end_time": "2022-01-11",
#                        "company_group_type": "group", "company_group_id": id}
#         f = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news',
#                              headers={"Authorization": token},
#                              json=RequestBody)
#         print(json.dumps(f.json(), indent=4, ensure_ascii=False))
#         assert jmespath.search('cn_name', f.json()) != ''
#
#     def shanchufenzu(self, token, id):
#         delete_FZ = {'id': id}
#         e = requests.request(method='get', url='http://123.56.138.96:3012/api/ainews-user/company-group/delete?',
#                              params=delete_FZ, headers={"Authorization": token})
#         print(json.dumps(e.json(), indent=4, ensure_ascii=False))
#         # assert jmespath.search('', e.json()) == True
#
#
# if __name__ == '__main__':
#     a = GSYQ()
#     a.tianjiafenzu()
#     a.tianjiagongsi()
#     a.more()
#     a.gongsiliebiao()
#     a.shanchufenzu()
