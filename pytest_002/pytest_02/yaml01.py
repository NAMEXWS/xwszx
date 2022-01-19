# import json
#
# import yaml
#
#
# def yaml_parser(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         return yaml.safe_load(f)
#
#
# def json_parser(path):
#     with open(path, 'r', encoding='utf-8') as f:
#         return json.load(f)
#
#
# a = yaml_parser('test_calculatur.yaml')
# print(a)
# b = json_parser('json01.json')
# print(json.dumps(b, indent=4, ensure_ascii=False))