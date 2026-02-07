'''
    yaml的操作：
        文件的读取
'''
import unittest
import yaml
from pathlib import Path
from parameterized import parameterized

"""
    将读取文件操作封装成一个函数：
        read_yaml 函数返回的是 YAML 文件解析后的 Python 对象（可能是字典或列表）。
        如果 YAML 文件的内容是一个字典（例如包含 fruits、numbers、users 等键），那么直接遍历这个对象会得到键名。
        需要访问每个键对应的值才能打印完整的数据。
"""
def read_yaml(filepath):
    """加载 YAML 测试数据"""
    with open(file=filepath, mode='r', encoding='utf-8') as f:
        values = yaml.safe_load(f)
    return values

values_list = read_yaml('./yaml/list.yaml')
values_dict = read_yaml('./yaml/dict.yaml')

# 打印 values_list 中的所有数据
for value in values_list:
    print(value)

print("————————————————————————————————————————————————————")



# 打印 values_dict 中的所有数据
for value in values_dict:
    print(value)

print("————————————————————————————————————————————————————")



# 打印search2.yaml中的数据（带有锚点）
values_search2 = read_yaml('./yaml/search2.yaml')
for value in values_search2:
    print(value)



# # 获取文件。open()之后一定给要记得关闭文件，但with open不需要
# file = open(r'./yaml/list.yaml', mode='r', encoding='utf-8')
# values = yaml.safe_load(file)
# print(values)   # ['a', 'b', 'c', 'd', 3, [1, 2, 3, 4, 5]]   这里的3是int。如果要将数字变成字符串，则在yaml中将数字加上''。即：'3'
# print(type(values)) # <class 'list'>