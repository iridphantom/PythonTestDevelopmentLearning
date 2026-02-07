"""
    Fixture运行机制：
        1. Fixture在运行时，有缓存机制：在用例执行时，Fixture可以有多次被调用。
            在第一次请求的时候，如果有返回值，则会通过这个返回值来实现后续的所有操作，而非重新运行。
        2. Fixture因为是函数，本质上也是代码的运行，所以在定义Fixture时，代码有可能会报错。
            ⚠如果在执行用例并关联Fixture的时候，Fixture产生了报错，则代码会终止运行，测试用例不会执行，返回error状态。
        3. Fixture只有被调用了，才会执行，否则不执行。
        4. Fixture默认不执行，但是只有一个参数，叫做autouse。
            默认为False，如果设置为True，则每一个用例执行前，都会调用该Fixture来执行。
            如果Fixture有return值，则完全没有autouse的意义存在。
            使用autouse的情况：

        若要调用Fixture返回的数据，则可以在测试用例中写fixture的名称，并基于fixture的名称，作为返回值的变量名，实现调用
"""
import pytest


# fixture的缓存机制：
@pytest.fixture
def a():
    return 'a'

@pytest.fixture(scope='session')
def b():
    print('这是b Fixture')
    return []

@pytest.fixture()
def c(a, b):    # Fixture本质是函数，所以没有return的时候返回None
    b.append(a)


# @pytest.fixture()
# def error():
#     2 / 0




def test_01(a,b,c):
    print(a)    # a
    print(b)    # ['a'] 缓存机制：
    print(c)    # 没有return，所以是none


# fixture因为重新调用了，所以会重新运行。
def test_02(b):
    print(b)


# # Fixture报错示例：
# def test_03(error): # 直接会报错，不执行测试用例
#     print("这是测试用例03")


def test_04():
    print("这是测试用例04")








if __name__ == '__main__':
    pytest.main(['-sv', './test_fixture_plus.py'])