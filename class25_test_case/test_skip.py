"""
    skip装饰器的应用：
        1. UnitTest和PyTest都具备skip功能。
        2. 将不需要执行的测试用例通过跳过的设置来执行。
            skip 无条件跳过  @pytest.mark.skip
            skipif 有条件跳过    @pytest.mark.skipif


    pytest运行时，它会先获取所有的测试用例，之后判断哪些要调过，哪些不要跳过。
"""
import sys

import pytest

a = 1

# 自定义跳过设置：如果python版本低于3.10，就提示跳过。（3是大版本，10是小版本。）
# 对于一些特殊的代码的运行，可以定义一些版本要求。（logging库中，3.8和3.10的有的参数定义是不一样的）
my_custom_skip = pytest.mark.skipif(sys.version_info < (3, 10), reason="Python版本过低，跳过")


@pytest.mark.skip('这是无条件跳过')
def test_class25_skip_func01():
    print("class25-测试用例01")


# 当条件为True，则执行skip操作
@pytest.mark.skipif(1 == 1, reason='这是skipif，条件为True')
def test_class25_skip_func02():
    print("class25-测试用例02")


# 当条件为False，则不会执行skip操作
@pytest.mark.skipif(1 == 2, reason='这是skipif，条件为False')
def test_class25_skip_func03():
    print("class25-测试用例03")


# 比对条件之前，pytest会先获取所有用例，并判断是否执行，a默认为1，即便后续有修改，但依旧会进行运行。
@pytest.mark.skipif(a == 2, reason="这是skipif，条件为False，但依旧运行")
def test_class25_skip_fun04():
    print("class25-测试用例04")


@my_custom_skip  # 自定义装饰器
def test_class25_skip_fun05():
    print("只有Python3.10以上才可以看到这段话")
