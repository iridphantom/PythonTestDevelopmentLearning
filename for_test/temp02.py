import unittest


class test_unittest(unittest.TestCase):
    def setUp(self):
        print("测试环境初始化，开始执行setup")

    def tearDown(self):
        print("测试执行完成，运行teardown")
        print("------------------------------")

    def test_a(self):
        print("开始执行test_a用例")

    def test_A(self):
        print("开始执行test_A用例")

    def test_1(self):
        print("开始执行test_1用例")

    def notest_1(self):
        print("不执行notest_1用例")


if __name__ == "__main__":
    unittest.main()