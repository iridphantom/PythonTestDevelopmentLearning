"""
    DDT的应用：
        1. 基于装饰器的形态，实现对模块的应用
        2. 只对调用ddt的class有效，只能对单个class产生作用
        3. 所有需要使用ddt的class，必须在class处提前声明ddt的调用，否则会报错。

"""
import unittest

from ddt import ddt, data, unpack, file_data

from class18_web_keys.web_keys import WebKeys


def read_file():
    values = []
    with open('yaml/data.txt', 'r', encoding='utf-8') as f:
        for line in f:
            values.append(line)
    return values


# ddt示例
@ddt
class TestDDT01(unittest.TestCase):  # 声明后，当前类中所有用例都可以使用ddt进行数据驱动和管理。
    """
        @data装饰器基于参数中有多少组数据，则对应的用例会执行响应的次数。
        在装饰器中，基于,进行数据的解析，最终基于数据的组数，执行对应次数的测试用例。

        @unpack装饰器实现对数据的二次解包：用于解包list或者元组。

            @data(['用户001', '密码001'], ['用户002', '密码002'])
            @unpack
            首先，基于,进行数据的第一次拆解，将,解析后获取两组不同的元素
            之后，@unpack进行数据的二次解包，基于,进行数据的二次拆分：
                ['用户001', '密码001']拆分为'用户001'和'密码001'这两个不同的数据
            然后基于用例所需参数，依照参数的顺序，依次传入用例之中。

        在UnitTest中，通过@data和@unpack可以管理简单的测试数据。如果数据一旦多起来，则不推荐使用。（因为维护太麻烦）
        在用例调用ddt之后，测试用例执行时会因为ddt而修改测试用例的名称。所以套件添加用例的方法里，无法基于测试用例名称实现对用例的添加。
            下面的测试用例名称在运行后，变成test_002_login_1__用户001__密码001__
    """

    # @data('用户001', '用户002', '用户003')  # data()方法，用于数据驱动，参数为数据列表。
    # def test_001_login(self, username):
    #     print("测试用例001-登录")
    #     print(username)

    # # 多参数据驱动：每组数据可以是元组或者列表
    # @data(['用户001', '密码001'], ['用户002', '密码002'], ['用户003', '密码003'])
    # @unpack # 二次解包数据
    # def test_002_login(self, username, password):
    #     print(username)
    #     print(password)

    # # 基于ddt实现文件读取操作：本质上是通过read_file()方法实现的文件内容读取，而非@data实现的
    # @data(*read_file())
    # def test_003_read(self, value):
    #     print(value)

    pass


@ddt
class TestDDT02(unittest.TestCase):
    # @file_data('./search.yaml')  # 专门用于解析yaml文件中的内容
    # def test_001_search(self, **kwargs):
    # driver = WebKeys('Chrome')
    # driver.open(kwargs['url'])
    # driver.input(**kwargs['input'])
    # driver.click(**kwargs['click'])
    # driver.wait(kwargs['wait_time'])
    # print(kwargs)
    """
               kwargs参数的内容：
               {'url': 'https://www.baidu.com',
                'input': {'by': 'id', 'value': 'chat-textarea', 'txt': 'ddt'},
                'click': {'by': 'id', 'value': 'chat-submit-button'},
                'wait_time': 5}
           """

    # 不使用**kwargs
    # @file_data('./search.yaml')  # 专用于解析yaml文件内容
    # def test_003_search(self, url, input, click, wait_time):
    #     driver = WebKeys('Chrome')
    #     driver.open(url)
    #     driver.input(**input)
    #     driver.click(**click)
    #     driver.wait(wait_time)

    pass


@ddt
class TestDDT03(unittest.TestCase):
    # 使用锚点
    @file_data('./search2.yaml')  # 专用于解析yaml文件内容
    def test_001_search(self, common, txt):
        driver = WebKeys('Chrome')
        driver.open(common['url'])
        driver.input(**common['input'], txt=txt)
        driver.click(**common['click'])
        driver.wait(common['wait_time'])


if __name__ == '__main__':
    unittest.main()
