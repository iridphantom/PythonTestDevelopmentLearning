"""
    ini配置文件读取：
        通过读取ini文件中的内容，实现代码的逻辑完整性。
        基于configparser来实现，也是官方自带库
"""
import configparser
import pathlib

# ini配置文件内容的读取
file = './email_conf.ini'
# 基于configparser实现文件内容的读取
conf = configparser.ConfigParser()  # 创建一个配置文件对象
conf.read(file) # 读取ini文件

# ini文件的内容获取
# values = conf.items('project')  # 默认返回list，内部的每一组数据都是一个独立的元组。
values = dict(conf.items('project'))  # 将配置文件的内容读取出来，转为dict格式。
print(values)   # 字典。{'sender': '2783523607@qq.com', 'receiver': '483983530@qq.com, nikola.yu.wang@outlook.com', 'pass_code': 'uqmypuziquxmdgdc'}

print(values['sender']) # 2783523607@qq.com

"""
    配置文件读出来默认是list嵌套元组的格式，转换为字典后，操作会更直观、有效
"""


# 封装ini文件的读取函数
def read(project_name):
    file = pathlib.Path(__file__).parents[0].resolve() / 'email_conf.ini'  # 获取配置文件
    conf = configparser.ConfigParser()
    conf.read(file)
    values = dict(conf.items(project_name))
    return values  # 一定记得return，否则无法正常使用获取到的数据内容