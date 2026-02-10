"""
    conftest.py文件的主要作用：
        1.管理所有的hook函数，实现pytest的功能增强以及二次修改
        2.用于管理整个测试过程中的所有Fixture
            可以让不同的文件实现对所有Fixture的正常调用。不用担心Fixture无法跨文件访问的作用域问题。
            conftest的作用域默认是 当前路径下的所有测试文件、子路径下的所有文件及文件夹。一般推荐将其放在测试用例根路径下
            session级别的Fixture都必须要放在conftest之中。
            autouse的Fixture也需要放在conftest之中。

"""
import pytest

@pytest.fixture
def hcc(request):
    def hcc_finalizer():
        print('hcc的后置执行')

    request.addfinalizer(hcc_finalizer)

    print('hcc的前置执行')



# 定义一个session级别的
@pytest.fixture(scope='session')
def session_hcc():
    print('这是session级别的Fixture')
    yield 'hcc'
    print('session的teardown')


# autouse的Fixture定义
@pytest.fixture(autouse=True)   # 当单次test session在执行的时候，所有的测试用例都会自动关联autouse=True，并且默认会自动执行。会在Function级别的前后置Fixture执行之前，先执行
def hcc_auto():
    print('这是autouse hcc')

"""


PS D:\Project\Python\hcc_python_class\class27_fixture_plus> pytest -sv             
================================ test session starts =================================
platform win32 -- Python 3.12.8, pytest-9.0.2, pluggy-1.6.0 -- D:\DevelopmentEnvironment\python3.12.8\python.exe
cachedir: .pytest_cache
rootdir: D:\Project\Python\hcc_python_class\class27_fixture_plus
plugins: repeat-0.9.4, xdist-3.8.0
collected 4 items                                                                     

test_cases/test_child.py::test_func 这是session级别的Fixture
这是auto use hcc
hcc child的前置执行
子路径下的Fixture调用
hcc
PASSEDhcc child的后置执行

test_hcc.py::test_hcc 这是auto use hcc
hcc的前置执行
hcc test case
hcc
PASSEDhcc的后置执行

test_teardown.py::TestDemo02::test_func01 这是auto use hcc
这是前置的执行内容
测试用例01
PASSED这是后置操作

test_teardown.py::TestDemo02::test_func02 这是auto use hcc
这是前置
ERROR这是teardown
session的teardown


"""