"""
    基于Fixture实现PyTest的前置操作：
        pytest中所有的前置都是基于Fixture来完成的，且Fixture默认的作用域是当前文件，默认情况下无法跨文件运行。
        如果要实现跨文件调用，则需要将Fixture定义在conftest.py之中，便可以实现对当前路径及子路径全部有效。
            前提：要先确认PyTest版本、文件命名是否规范。

        PyTest启动的时候，会产生一个session对象，来管理本次所要执行的所有测试用例。所以本次执行的代码，都是基于当下的session来统一管理的。

        Fixture定义作用域可以分为以下不同的等级：
            1. session级别    整个测试session中都有效。只会在第一次调用的时候执行一次，后续调用都是基于已有的数据来继续执行。
            2. module级别     整个py文件执行一次
            3. class级别      整个class执行一次
            4. function级别   每一个测试用例执行一次，是scope的默认等级

"""
import pytest

# 第一种pytest的前置定义：

# # session级别
# @pytest.fixture(scope='session')
# def session_func():
#     print('这个是session级别')
#
#
# # module级别
# @pytest.fixture(scope='module')
# def module_func():
#     print('这个是module级别')
#
#
# # class级别
# @pytest.fixture(scope='class')A
# def class_func():
#     print('这个是class级别')
#
#
# # function级别，是默认级别
# @pytest.fixture
# def function_func():
#     print('这个是function级别，且是默认级别')
#
#
# class TestDemo: # 注意PyTest的命名规则
#     def test_01(self, session_func, module_func, class_func, function_func):
#         print('这是测试用例01')
#
#     def test_02(self, session_func, module_func, class_func, function_func):    # 只执行了function_func
#         print('这是测试用例02')
#
#
# if __name__ == '__main__':
#     pytest.main(['-sv', './test_setup.py'])


# --------------------------------------------------------

# 第二种pytest的前置定义。个人不太推荐。
# 请不要使用这种方式 请不要使用这种方式 请不要使用这种方式 请不要使用这种方式
# class TestDemo:
#     def setup_method(self):  # function级别
#         print('这是setup')
#
#     def setup_class(self):  # class级别
#         print('这是class setup')
#
#     def test_01(self):
#         print('测试用例01')
#
#     def test_02(self):
#         print('测试用例02')


# --------------------------------------------------------

"""
    Fixture的参数传入：
        如果要解决Fixture传参的操作：
            1. 基于Fixture需要的数据，通过其他的Fixture传入进来。
            2. 通过request来接收外部传入的数据
"""

# 基于request实现对外部数据的传入操作
@pytest.fixture()
def demo(request):
    name, value = request.param  # request是固定名称，不允许修改。
    print('这是Fixture数据的传入')
    print(f"name: {name}")
    print(f"value: {value}")


# 用例传入数据
@pytest.mark.parametrize('demo', [['name参数', 'value参数']], indirect=True)  # indirect=True表示为调用的是Fixture，而非普通参数
def test_01(demo):
    print('这是测试用例')
    print(demo) # 由于Fixture的默认级别是function，每一个测试用例执行一次，所以打印的时候是none。


if __name__ == '__main__':
    pytest.main(['-sv', './test_setup.py'])