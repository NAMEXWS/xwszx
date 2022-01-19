# import json
#
# import requests
#
#
# class Test_GSYQ:
#     def test_001(self, header):
#         a = {"name": "薛习针tot"}
#         c = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-user/company-group/create',
#                              headers=header,
#                              json=a)
#         print(json.dumps(c.json(), indent=4, ensure_ascii=False))
#
#     def test_tianjiagongsi(self, id, header):
#         a = {"company_code": "000001", "group_id": id}
#         d = requests.request(method='post',
#                              url='http://123.56.138.96:3012/api/ainews-user/company-group/company-create',
#                              headers=header,
#                              json=a)
#         print(json.dumps(d.json(), indent=4, ensure_ascii=False))
#
#     def test_more(self, header):
#         a = {"start_time": "2022-01-04T17:22:16", "end_time": "2022-01-11T17:22:16", "page": 1,
#                        "pagesize": 20}
#
#         e = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news',
#                              headers=header,
#                              json=a)
#         print(json.dumps(e.json(), indent=4, ensure_ascii=False))
#
#     def test_gongsiliebiao(self, id, header):
#         a = {"page": "1", "page_size": 10, "order_by": "", "order_type": "DESC", "cp_type": "",
#                        "board": "",
#                        "keyword": "", "is_new_data": 0, "classification": "", "category_key": "", "min_score": 0,
#                        "max_score": 100, "start_time": "2021-12-28", "end_time": "2022-01-11",
#                        "company_group_type": "group", "company_group_id": id}
#         f = requests.request(method='post', url='http://123.56.138.96:3012/api/ainews-espy/api/opinion/flash-news',
#                              headers=header,
#                              json=a)
#         print(json.dumps(f.json(), indent=4, ensure_ascii=False))
#
#     def test_shanchufenzu(self, id, header):
#         delete_FZ = {'id': id}
#         e = requests.request(method='get', url='http://123.56.138.96:3012/api/ainews-user/company-group/delete?',
#                              params=delete_FZ, headers=header)
#         print(json.dumps(e.json(), indent=4, ensure_ascii=False))
