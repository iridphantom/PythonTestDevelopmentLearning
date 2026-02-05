"""
    什么是Fixture？
        夹具，在PyTest中，可以通过Fixture来实现对前置和后置的内容完成。属于UnitTest的前后置的强化版本。


    测试基础概念(测试步骤）：
        1. 准备环境。准备数据。
        2. 基于已有的数据进行实际的测试执行
        3. 校验测试结果
        4. 资源释放


    Fixture基本应用：
        1. Fixture是基于函数的形态来实现的，调用的时候，通过函数名称来进行调用。
        2. Fixture定义时，需要通过Fixture的装饰器来进行声明。
        3. 因为Fixture本身属于函数，所以可以通过return来实现对需要获取的内容进行返回，在用例中可以直接调用return的数据
        4. 在用例中，可以同时调用多个Fixture来实现测试用例内容的完善。
        5. 调用Fixture是通过在用例中定义形参，形参名称必须与Fixture保持一致。
        6. Fixture的运行顺序是基于用例中形参的顺序依次执行。例：(fixture_demo01, fixture_demo02)，先执行01，再执行02
        7. Fixture一定是先于测试用例来执行的。基于形参，先去找有没有对应的fixture。有的话，就先执行fixture，再执行测试用例。
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
    Fixture示例：
"""

# @pytest.fixture
# def fixture_demo01():  # 普通函数转换为Fixture
#     print("这是Fixture的定义函数01")
#     return '这是Fixture的返回数据'    # return的数据想要在用例使用，直接通过Fixture的名称来调用
#
# @pytest.fixture
# def fixture_demo02():  # 普通函数转换为Fixture
#     print("这是Fixture的定义函数02")
#
#
# # 调用Fixture：参数中输入fixture的名称（方法名）即可。
# def test_demo01(fixture_demo01, fixture_demo02):
#     print("这是测试用例")
#     print(fixture_demo01)   # 这里的"fixture_demo01"只是取了return的值，并不是调用了一次fixture。注意要在参数中传入fixture，才能调用


# ---------------------------------------------------------------------------------------------

"""
    fixture在测试过程中的应用实操：
"""

@pytest.fixture(scope="session")    # scope="session"的作用：测试用例执行过程中，只执行一次。
def browser_driver():   # 创建一个driver的fixture
    service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    return driver


# fixture调用Fixture和Fixture在用例中执行其实是一样的。都是可以互相调用。
@pytest.fixture()
def open(browser_driver):   # fixture调用fixture：fixture本质是函数，这里可理解为函数调用函数。
    browser_driver.get("https://www.baidu.com")


def test_01(browser_driver, open):  # browser_driver、open是fixture的名称。
    browser_driver.find_element('id', 'chat-textarea').send_keys('schillernd')
    time.sleep(5)

def test_02(browser_driver):
    browser_driver.get("https://www.jd.com")    # 加上了scope之后，测试用例会使用同一个测试用例。




if __name__ == '__main__':
    pytest.main(['-sv'])