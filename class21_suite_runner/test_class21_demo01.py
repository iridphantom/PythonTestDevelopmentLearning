"""

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
            raise   # 添加异常处理，不影响测试用例的结果：在except之中添加raise关键字。


class TestDemo02(unittest.TestCase):    # 不会调用TestDemo01中的代码
    def test_01(self):
        print('这是TestDemo02的test_01测试用例')


if __name__ == '__main__':
    unittest.main()
    # TestDemo.test_demo01()