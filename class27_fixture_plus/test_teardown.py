"""
    基于Fixture来实现teardown相关操作：
       1.一定是基于Fixture来实现teardown。
       2.有两种不同的teardown实现效果：
            ①.基于关键字yield来实现。（yield是一个生成器）
                yield接口既可以return数据，也可以让函数挂起，暂停运行，从而满足到teardown的特殊要求。
                核心：通过yield的挂起机制。当setup执行完成后，通过yield来实现挂起，在用例执行结束后，再调用yield后续的内容，从而满足teardown的需要。

                yield本身的实现是依托于python的运行机制。当Fixture报错时，yield之后的代码就不会继续执行，从而产生风险。
                如果前置内容非常简单，则yield非常好用。

            ②.基于finalizer()来实现——推荐，它更为严谨
                finalizer()能够解决yield如果出现报错则无法继续执行的风险。
                teardown的代码块一定要在setup之前。因为代码运行是自上而下的。所以先注册teardown，才能够确保即便setup出错，也能够正常执行teardown。

                finalizer示例：
                    def demo(request): # request不可修改，是固定的名称
                        # 定义teardown内容
                        def demo_finalizer():   # 建议名称在原有函数名后方添加_finalizer()，表明是teardown
                            teardown代码块
                        request.addfinalizer(demo_finalizer) # 函数名称不要加括号，目的是让pytest将其识别为teardown

                        # setup内容
                        setup代码块
                        return 需要的数据

"""
import pytest


"""
    yield示例：
    虽然使用yield可以实现用例级别的前后置操作，但是不太推荐。
    因为Fixture它本身是一个函数，由于函数本身会执行一些逻辑，我们在函数中所写的一些代码块，函数在执行时，有可能会因为我们传入的数据 / 执行的流程，产生报错，从而导致测试用例终止。
"""

# @pytest.fixture()
# def demo():
#     print('这是前置的执行内容')  # 前置
#     # 1 / 0   # 遇到报错-->结束运行。
#     yield 223  # 这里会挂起函数；当函数执行结束后，会继续调用未执行的操作
#     print('这是后置操作')  # 后置
#
# class TestDemo01:
#     def test_func01(self, demo):
#         print('这是测试用例01')
#         print(demo) # 打印yield返回数据
#
#     def test_func02(self, demo):  # 由于scope默认值为function，所以还会再调用demo方法
#         print('这是测试用例02')
#
# if __name__ == '__main__':
#     pytest.main(['-sv', './test_teardown.py'])



# ---------------------------------------------------------




"""
    finalizer()示例：
    推荐，更为严谨。
"""
@pytest.fixture()
def demo_start():
    print('这是yield的前置执行内容')
    yield 233
    print('这是yield的后置执行内容')

@pytest.fixture()
def demo_final(request): # 注意：teardown要放在上面
    # 定义teardown的内容
    def demo_final_finalizer():
        print('这是finalizer后置执行内容')
    request.addfinalizer(demo_final_finalizer)  # 注册teardown

    # 定义前置内容
    print('这是finalizer前置执行内容')
    12 / 0
    return 123  # 不需要yield来实现数据返回了。


class TestDemo02:
    def test_func01(self, demo_start):
        print('测试用例01')

    def test_func02(self, demo_final):
        print('测试用例02')



if __name__ == '__main__':
    pytest.main(['-sv', './test_teardown.py'])