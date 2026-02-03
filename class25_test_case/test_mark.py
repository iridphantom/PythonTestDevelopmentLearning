"""
    mark装饰器：
        在pytest管理测试用例的时候，可以针对不同的用例，进行自定义的分类设置，让测试用例进行更加精细化的管理。
        区分不同的业务流程下的测试用例或者说各种模块下的测试用例内容，基于mark进行分类之后，结合实际情况选择性运行特定分类下的代码。

    mark装饰器的使用：
        1. @pytest.mark实现对用例进行标记
        2. 可以实现对用例进行标记分类的作用
        3. 运行指定的标记测试用例，需要调用-m指令，指令支持逻辑运算符
            -m 标记名称 执行指定标记名称的所有用例
            -m "login or register"   执行login标记或者是register标记的测试用例
            -m "login and register"  执行标记为login且同时为register的测试用例
            -m "not login" 执行标记不为login的测试用例
        4. -m指令下的标签名称选择，一定要用双引号""括起来，否则识别会出问题。
        5. 标签名称不要太复杂，尽可能简单，方便标签的管理。
"""
# mark装饰器使用示例：

import pytest

@pytest.mark.login
def test_class25_mark_func01():
    print("class25-mark-测试用例01-login")

@pytest.mark.register
def test_class25_mark_func02():
    print("class25-mark-测试用例02-register")


# 多个标记的使用：是不同标记名称都分别使用pytest.mark来进行标记
@pytest.mark.asd
@pytest.mark.fgh
def test_class25_mark_func03():
    print("class25-mark-测试用例03")



def test_class25_mark_fun04():
    print("class25-mark-测试用例04")


def test_class25_mark_fun05():
    print("class25-mark-测试用例05")
