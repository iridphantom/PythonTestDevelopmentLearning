"""
    Parametrize装饰器:
        主要是用于对测试用例实现数据驱动的功能。
        可以管理简单的测试数据，也可以通过导入测试文件的数据内容来实现复杂数据的传递功能。
        ddt可以用在pytest，但是不建议使用。（DDT最佳搭档就是UnitTest）


    Parametrize装饰器的应用：
        1. 基于@Pytest.mark.parametrize来实现调用的。
        2. 参数介绍：
            ①.参数1；必须与用例形参保持完全相同。
            ②.参数2；必须是list格式。
        3. 多参数下，如果通过多个Parametrize实现数据传递，则pytest会采用交集的计算方式实现数据的传入
        4. 多参数下，如果通过一个Parametrize传入所有数据，则会基于合并之后的数据进行传入和解析。
        5. 所有的数据，都是基于Parametrize中定义的形参顺序依次传入的。
        6. 如果从外部获取数据：
            ①. 方法一：定义一个list的数据变量，进行传入
            ②. 方法二：获取文件内容，进行传入
"""
import pytest
import yaml


# Parametrize装饰器使用示例
@pytest.mark.parametrize('a', [1, 2, 3])
def test_class25_parametrize_func01(a):
    print("class25-parametrize-测试用例01")


# 多装饰器：
# 多参数下，如果通过多个parametrize实现数据传递，则pytest会采用交集的计算方式实现数据的传入。
@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', ['a', 'b', 'c'])
def test_class25_parametrize_func02(a, b):
    print("class25-parametrize-测试用例02")


@pytest.mark.parametrize('b,a', [(11, 22), (33, 44)])  # 这一步进行赋值，按照顺序赋值，之后传入。
def test_class25_parametrize_func03(a, b):
    print(f"a:{a}")
    print(f"b：{b}")


# 从外部变量获取数据 方法一：
data = [1, 2, 3, 4, 5]
@pytest.mark.parametrize('a', data)
def test_class25_parametrize_func04(a):
    print(a)


# 从外部文件获取数据 方法二：
# pytest无法直接读取yaml文件，需要通过yaml.safe_load()方法进行读取。
# 也可以封装一个yaml文件的读取函数，在此处调用。
"""
    test_parametrize.py::test_class25_parametrize_func05[user_data0] {'name': 'potato-chip', 'password': 123456}
    PASSED
    test_parametrize.py::test_class25_parametrize_func05[user_data1] {'name': 'nugget', 'password': 'asdfgh'}
    PASSED
    
    这里的[user_data0]、[user_data1]其实就是ids，并且ids可以自定义。步骤：①添加ids=[xxx] ②.在装饰器中添加ids=ids。
    作用：可以为测试用例进行一些描述。
    ids默认不支持中文显示。但可以进行修改。(conftest.py中。暂时不需要掌握。）
"""
ids = ['first_run第一', 'second_run第二']


@pytest.mark.parametrize('user_data', yaml.safe_load(stream=open('./user.yaml', mode='r', encoding='utf-8')), ids=ids)
def test_class25_parametrize_func05(user_data):
    print(user_data)


# parametrize特定参数组的添加
@pytest.mark.parametrize('a,b', [(1, 2), pytest.param(33, 44)], ids=['第一轮', '第二轮'])
def test_class25_parametrize_func06(a, b):
    print(f"a:{a}")
    print(f"b：{b}")




# pytest ./test_parametrize.py -sv -k test_class25_parametrize_func06