"""
    基于Fixture来实现teardown相关操作：
       1.一定是基于fixture来实现teardown。
       2.总计有两种不同的teardown实现效果：
            ①.基于关键字yield来实现。（yield是一个生成器）
                yield接口已return数据，也可以让函数挂起，暂停运行，从而满足到teardown的特殊要求。
                核心：通过yield的挂起机制。当setup执行完成后，通过yield来实现挂起，在用例执行结束后，再调用yield后续的内容，从而满足teardown的需要。
            ②.基于finalizer()来实现

"""
import pytest


"""
    yield示例
"""
@pytest.fixture
def demo():
    print('这是前置的执行内容')  # 这是前置
    yield
    print('这是后置操作')  # 这是后置

def test_func01(demo):
    print('这是测试用例01')

def test_func02(demo):      # 由于scope默认值为function，所以还会再调用demo方法
    print('这是测试用例02')

if __name__ == '__main__':
    pytest.main(['-sv', './test_teardown.py'])