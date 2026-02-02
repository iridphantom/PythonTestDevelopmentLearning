"""
    PyTest基本应用：
        1. PyTest是基于类和方法来实现对用例的管理。可以通过类来管理，也可以直接通过方法来进行管理。具体看你是如何设计用例结构的。
        2. 不需要继承于任何内容，直接运行即可。（使用UnitTest需要继承于unittest.TestCase类）
        3. PyTest中没有默认的运行顺序，运行顺序就是谁先定义谁先运行。
        4. PyTest是基于指令来运行的。
            可以在main()中，通过pytest.main()来执行，也可以在cmd中通过指令来执行。（指令： pytest -sv ...）（-s -v基本上必加，可简写为-sv）
            ①. -s 表示将print的内容显示在控制台之中。
            ②. -v 表示将运行的日志显示在控制台有更加详细的内容。
            ③. 指定文件 / 类 / 测试用例执行：
                test_pt.py::TestDemo01::test_func03，test_pt.py文件下的TestDemo01类下的test_func03用例。
                常规情况下的文件路径依旧是基于/来区分。只有类和方法的层级是基于::进行区分。
            ④. -k 表示只执行包含有指定字符串的测试用例。类似于模糊查找的概念。
            ⑤. -q 静默运行
            ⑥. -x 表示如果当前用例报错了，本次运行直接终止，未运行的测试用例不再执行。（适用于pom）
            ⑦. --maxfail=num 如果用例执行过程中报错总数达到num值时，本次运行结束。
            ⑧. -n num，表示用例的多线程执行，num表示启动的线程数量。(需要安装库：pip install pytest-xdist）
            指令一般分为字母和单词的形式。PyTest中，字母指令为-，单词指令为--
        5. PyTest在执行时需要指定路径。根据路径来获取当前符合条件的所有测试用例文件及用例内容。
        6. PyTest下的断言都是基于assert来实现的。
        7. 所有的PyTest运行指令，都可以基于控制台指令来实现，也可以基于pytest.main([])方式来实现。更推荐控制台指令来运行


"""
import pytest


class TestDemo01:
    def test_func01(self):
        print("这是测试用例01")

    def test_func03(self):
        print("这是测试用例03")

    def test_func02(self):
        print("这是测试用例02")

class TestDemo02:
    def test_demo02_func1(self):
        print("这是测试用例2.1")

    def test_demo02_func3(self):
        print("这是测试用例2.3")

    def test_demo02_func2(self):
        print("这是测试用例2.2")

if __name__ == '__main__':
    pytest.main(['-sv', '-k test_demo'])