'''
    断言校验的实现：
        1. 断言基本都是基于assert关键字来实现的。
            assert 表达式,message
                1. 表达式： 当断言表达式为True，则断言通过，程序无任何问题。为False时，程序抛出断言异常。显示message
                2. Message：显示报错信息，自定义str内容。
    断言最常见的手段就是判断某个元素的文本信息。除此之外，还可以使用元素是否存在于页面来进行断言。
    所以显式等待除了做常规等待之外，也可以适用于断言的特定场景。
'''
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
# assert示例：
assert 1 == 1, "断言失败"

assert 1 == 2, "断言失败，断言表达式错误"
"""

# 准备环境与测试数据.用的是他人的代码
user = '23456789@qq.com'
password = '123456'

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# 设置隐式等待时间，最长为5秒
driver.implicitly_wait(5)

driver.maximize_window()
# 访问url
driver.get('http://fecmall.com/customer/account/login')  # 自动化执行过程中，能够省略的步骤直接省略。

# 输入账号密码
driver.find_element('id', 'email').send_keys(user)
driver.find_element('id', 'pass').send_keys(password)

"""
断言示例
"""
# 获取实际结果
reality = driver.find_element('xpath', '//div[@class="box-content"]/div/span').text  # text是获取指定元素的文本信息

"""
# 基于日志进行断言信息的输出方式之一。
try:
    assert user == reality, f'''
    你的预期结果是{user}，你的实际结果是{reality}，两者不相等

    预期结果为：{user}，
    实际结果为：{reality}，
    断言结果：{user} != {reality}
    '''
    # 输出正常通过的日志

except:
    # 输出错误日志
    raise
"""


"""
# 显式等待用于断言的场景。
WebDriverWait(driver, 5, 0.5).until(
    lambda element: driver.find_element('xpath', '//div[@class="box-content"]/div/span1'),
    message='登录失败，元素不存在'
)
"""

time.sleep(5)