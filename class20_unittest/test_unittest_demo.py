"""
    UnitTest的语法规则与基本应用：
        1. 所有的测试用例文件，必须以test_开头。格式：test_*.py
        2. 所有的UnitTest相关内容，必须要写在class(也就是类)中。class必须要继承于UnitTest.TestCase类。类名必须以Test开头
        3. 测试用例：
            ①. 都是基于【方法】的结构形态来实现的。方法名称必须以test_开头作为命名。否则无法识别为测试用例
            ②. 所有的测试用例在执行的时候，都是基于main之中，通过unittest.main()方法来运行。
            ③. UnitTest不需要实例化，可以直接运行；而且用例之间虽然可以相互调用，但是没有意义。
            ④. 用例在执行的时候，基于先后顺序，不需要考虑单个用例的逻辑补足，每一个用例在执行时，彼此都会产生基本关联。
                在基于UnitTest实现用例定义时，我们在设计时必须要考虑尽可能降低用例之间的关联性
            ⑤. Unittest之中，用例的执行有它自己的默认排序规则:
                规则定义是0-9,a-z,A-Z的排序规则。规则固定不变的（除非修改UnitTest的源代码）
                推荐的用例命名规范：（最终还是要以公司的编码规范要求为首要定义。）
                    test_编号_业务名称()
                    test_01_login()
            ⑥. 测试用例虽然是方法的结构，但是不推荐使用return。避免用例之间的相互调用。
               如果需要关联到用例产生的数据，建议【以成员属性赋值的方式】来完成。
            ⑦. 用例总计有三种不同的状态：
                1. Pass 通过
                2. Failed 失败    是用例中的【断言】执行失败
                3. Error 错误     用例执行时代码出现报错（非断言报错），error状态只有测试报告会显示。
                用例的成功与否，是基于用例代码是否报错来界定的。所以我们在用例之中基本不会使用try...except语法。因为如果使用了try...except捕获异常，框架会认为用例执行成功（Pass），但实际上可能存在逻辑错误。
                如果非要加异常处理，又不想影响测试用例的结果，可以在except之中添加raise关键字。
            ⑧. 断言机制：
                所有的断言，都是基于self.assert*()来实现的。

        4. 前置与后置条件的使用：
            ①. 测试场景：
                准备测试数据，准备测试环境
                基于数据与环境，实现用例的执行------}UnitTest解决的东西
                基于测试结果，进行断言校验---------}UnitTest解决的东西
                清空脏数据，还原环境。
            ②. 前置:————准备测试数据，准备测试环境
                前置的方法名称是固定的，不可以修改。相同作用域下的前置方法只能有一个。（因为前置的方法名称是固定的，而python的语法不支持方法的重载。若定义多个前置条件，则会使用最后的前置方法）
                作用域分为：用例级和类级
                    用例级：每一个测试用例都会执行。setUp()
                    类级：每一个测试类只会执行一次。setUpClass(cls)
            ③. 后置：————清空脏数据，还原环境
                与前置相同。
                    用例级：tearDown()
                    类级：tearDownClass(cls)

    每一个UnitTest类，都是独立存在的个体，类彼此之间不会有任何关联。类作为用例管理的唯一单位。

    测试业务管理：
        1. 基于类来实现流程的管理————不同的业务流程，使用不同的类。
            ①. 基于一个用例实现完整的业务流程
            ②. 基于不同的用例实现不同的子流程，基于用例执行顺序最终拼接成完整业务流程。例：下单拆分为：登录 -> 找到商品 -> 加购 -> 选择加购的商品 -> 支付
            推荐②，因为可以细化测试用例。定义好前后置条件后，方便用例的管理和维护
        2. 一个py文件有多个类和一个py文件关联一个类。
            推荐后者，便于代码的管理和维护
"""
import unittest


# UnitTest使用规范定义
class TestDemo01(unittest.TestCase):
    # 属性定义
    attr1 = None

    # 类级前置与后置
    @classmethod
    def setUpClass(cls):
        print('=== 这是【类级】前置条件 ===')

    @classmethod
    def tearDownClass(cls):
        print('=== 这是【类级】后置条件 ===')

    # 用例级前置
    def setUp(self):
        print("这是【用例级】前置条件")

    # 用例级后置
    def tearDown(self):
        print("这是【用例级】后置条件")


    # 测试用例
    def test_demo(self):
        print("这是一条测试用例")

    def test_demo01(self):
        print("这是测试用例01")

    def test_demo03(self):
        try:
            print("这是测试用例03")
            assert 1 ==0
        except:
            raise

    def test_demo02(self):
        self.fun1()
        print("这是测试用例02")
        TestDemo01.attr1 = 1  # 笔记的第6点，属性赋值的方式实现数据的互通，但是要注意用例的执行先后顺序。
        self.fun2(2)    # 本该报错的用例，但是用例执行成功。



    # 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例
    # 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例
    # 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例 非测试用例
    def fun1(self):
        print("这不是一条测试用例")

    def fun2(self, num):
        try:
            assert 1 == num
        except:
            print("处理异常")
            raise


class TestDemo02(unittest.TestCase):    # 不会调用TestDemo01中的代码
    def test_01(self):
        print('new test case')


if __name__ == '__main__':
    unittest.main()
    # TestDemo.test_demo01()