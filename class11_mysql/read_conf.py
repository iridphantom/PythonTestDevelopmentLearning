import configparser
import pathlib


def read(project_name):
    file = pathlib.Path(__file__).parents[0].resolve() / 'mysql_conf.ini'
    conf = configparser.ConfigParser()
    conf.read(file)
    values = dict(conf.items(project_name))
    # 读取文件内容的时候，很容易遇到你所期望的数据类型与实际的数据类型有偏差。很多时候我们需要对数据进行二次修改.
    # 当获取到key为port的时候，value就需要转型为int类型。其余的key不需要做任何修改操作.
    for key, value in values.items():
        if key == 'port':
            values[key] = int(value)    # 获取到的value是str类型，需要转为int类型。
    return values

print(read('ONLINE_ENV'))