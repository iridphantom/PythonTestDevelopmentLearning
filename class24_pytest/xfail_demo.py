"""
    xfail装饰器：针对异常用例的管理手段
        在执行测试用例的时候，其实我们已经有了明确的预期，即哪些用例就会执行失败，哪些用例就会成功。
        对于明确已知会失败的用例，标注xfail，就可以明确知道用例的预期结果是失败的。
        当用例执行真的失败了，则返回xfail状态；如果执行成功，就返回xpass状态。

        @pytest.mark.xfail装饰器的参数:
            condition：是一个表达式，当为True时，则xfail生效；否则不生效。
                1. condition：表示表达式，当为True时，xfail通过，提示为xpass状态，若为failed,则不执行
                2. reason:当xfail装饰器生效时，显示的error信息
                3. run，默认为True，可手动修改为False。代表是否需要执行xfail装饰器的用例
                4. strict，默认为Failed，可修改为Ture。用例执行时，如果用例运行成功，xfail对应的测试用例就会显示为error状态

                当某个功能点没完成但用例已经写好 / 还未运行 / 现阶段还不需要的运行的测试用例，可以定义一个xfail装饰器，用于返回xfail状态

        xfail的另外一种调用形态：
            可以通过pytest.xfail()来实现对其进行调用。如果该方法被调用，则返回xfail结果，当前用例的后续内容不再继续执行。

        --runxfail指令：用于将所有已标记为xfail状态的测试用例，转变为正常的测试用例。返回pass和failed状态
"""
import pytest


# xfail示例
@pytest.mark.xfail(1 == 1, reason='这是reason')
def test_01():
    a = 2
    assert a == 3

@pytest.mark.xfail
def test_02():
    print(1+1)
    b = 2
    assert b == 2

@pytest.mark.xfail(strict=True)
def test_03():
    print(1 + 2)


def test_04():
    for i in range(0, 10):
        print(i)
        if i == 5:
            pytest.xfail('这是xfail的第二种调用')


if __name__ == '__main__':
    pytest.main()

# cmd: pytest .\xfail_demo.py -sv --runxfail