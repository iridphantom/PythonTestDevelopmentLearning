"""
        assert断言机制：
        1. pytest中都是使用assert实现断言。
        2. assert本身的内容定义，在pytest会有完整的信息展示，所以不需要额外去进行定义更详细内容。（pytest会给出断言失败的错误信息）
        3. 用例在执行失败之后，pytest具备用例失败重跑机制。（使用示例：存在网络条件可能影响测试结果的情况下，可以使用失败重跑。就比如VPN连接特定网络）
            通过指令--lf（全称叫做 last failures）来实现，将上一次失败的用例全部重新执行一次

            --ff指令。（全称叫做failures first），将所有的用例全部执行，但是失败的用例优先执行。

            --count=num，用例执行次数。在执行测试用例的时候，通过手动设置num数值，来让用例执行规定的总次数。
            一般是结合--lf一同使用。实现所谓的用例重跑机制。失败用例多次执行。
            count指令如果要使用，需要提前添加库：pip install pytest-repeat

        --lf和--ff指令，是否能够应用，优先取决于你的用例设计结构上来定义。
        当一个用例写一个完整的流程，--ff就可以有帮助；当将一个流程拆分成不同的子流程，子流程按照顺序写到测试用例里，这样就不可以使用
"""

def test_01():
    assert 1 == 2


def test_02():
    assert 1 == 0


def test_03():
    assert 1 == 1


def test_04():
    assert 1 == 4


"""
pytest ./test_assert.py -sv --lf


platform win32 -- Python 3.12.8, pytest-9.0.2, pluggy-1.6.0 -- D:\DevelopmentEnvironment\python3.12.8\python.exe
cachedir: .pytest_cache
rootdir: D:\Project\Python\hcc_python_class\class25_test_case
plugins: xdist-3.8.0
collected 4 items / 1 deselected / 3 selected                                                                                                                               
run-last-failure: rerun previous 3 failures

test_assert.py::test_01 FAILED
test_assert.py::test_02 FAILED                                                                                                                                              
test_assert.py::test_04 FAILED
"""



"""
pytest ./test_assert.py -sv --ff


platform win32 -- Python 3.12.8, pytest-9.0.2, pluggy-1.6.0 -- D:\DevelopmentEnvironment\python3.12.8\python.exe
cachedir: .pytest_cache
rootdir: D:\Project\Python\hcc_python_class\class25_test_case
plugins: xdist-3.8.0
collected 4 items                                                                                                                                                          
run-last-failure: rerun previous 3 failures first

test_assert.py::test_01 FAILED
test_assert.py::test_02 FAILED
test_assert.py::test_04 FAILED
test_assert.py::test_03 PASSED
"""