'''
    WebUI关键字驱动类实现
        1.本身属于逻辑代码类。
        2.Selenium的二次封装：优先封装居于业务需求或者最常见的操作行为，以此作为关键字来使用。
          例如：
            访问URL
            点击
            输入
            查找元素
            关闭
            ....
        关键字驱动类不需要十全十美，因为实际业务场景下是多变的，只需要考虑系统需要什么，我们就封装什么。
        如果有缺失，自己再补充就可以了。

        逻辑代码本身只负责逻辑代码的封装，运行文件不会有任何的作用。逻辑代码一定是在调用时才会产生实际价值
'''
import time

import ddddocr
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from class17_options.options import options, firefox_options


# 关键字驱动类实例

# 创建浏览器对象
def open_browser(browser_type):
    # if browser_type == 'Chrome':
    #     driver = webdriver.Chrome()
    # elif browser_type == 'Safari':
    #     webdriver......

    # 基于反射实现浏览器生成，也就是对上面的优化
    try:
        if browser_type == 'Chrome':
            service = Service(r'D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe')
            driver = webdriver.Chrome(service=service, options=options())
        elif browser_type =='FireFox':
            service = Service(r'D:\DevelopmentEnvironment\BrowserDrivers\geckodriver.exe')
            driver = webdriver.Firefox(service=service, options=firefox_options())
        else:
            # browser_type.capitalize()：将浏览器类型首字母大写，例如 "chrome" → "Chrome"
            # getattr(webdriver, ...)：从 webdriver 模块中获取指定名称的属性/类，相当于动态调用 webdriver.Chrome 或 webdriver.Edge 等
            driver = getattr(webdriver, browser_type.capitalize())()    # 动态创建浏览器
            print("asd")
    except (AttributeError, WebDriverException) as e:
        print(f"浏览器启动失败: {e}")
        driver = webdriver.Chrome()     # 生成没有任何浏览器配置的Chromedriver对象
    """
    except:
        driver = webdriver.Chrome()  # 生成没有任何浏览器配置的Chromedriver对象
    """
    return driver

    # 方法2：基于匹配机制实现浏览器生成：具体方案内容，大家课后可以尝试补足逻辑
    # browsers = {
    #     'Chrome': ['gc', 'google chrome', 'chrome', 'Chrome', '谷歌浏览器'],
    #     'Edge': ['Edge', 'edge'],
    #     'FireFox': ['FireFox', 'firefox', '火狐']
    # }
    # for key, value in browsers.items():
    #     if browser_type in value:
    #         driver = getattr(webdriver, key)()
    #         return driver


class WebKeys:
    # 临时的driver对象
    # service = Service(r'D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe')
    # driver = webdriver.Chrome(service=service, options=options())

    # 构造方法
    def __init__(self, browser_type):
        self.driver = open_browser(browser_type)

    # 封装访问URL：
    def open(self, url):
        self.driver.get(url)

    # 封装定位元素
    def locator(self, by, value):
        return self.driver.find_element(by, value)

    # 封装输入
    def input(self, by, value, txt):
        self.locator(by, value).send_keys(txt)

    # 封装点击
    def click(self, by, value):
        self.locator(by, value).click()

    # 封装关闭
    def quit(self):
        self.driver.quit()

    # 封装强制等待
    def wait(self, wait_time):
        time.sleep(int(wait_time))


    # 断言
    #     def assert_text(self, by, value, expected):
    #         reality = self.locator(by, value)
    #         assert reality == expected, f'''
    #         预期结果未匹配，请检查！
    #         预期结果为：{expected}
    #         实际结果为：{reality}
    #         断言结果：{expected} != {reality}
    # '''
    def assert_text(self, by, value, expected):
        # 1. 首先定位到元素
        element = self.locator(by, value)  # 这里返回的是 WebElement 对象

        # 2. 从元素对象中获取文本
        reality = element.text  # 关键：调用 .text 属性获取文本内容

        # 3. 比较获取到的文本和预期文本
        assert reality == expected, f'''
        预期结果未匹配，请检查！
        预期结果为：{expected}
        实际结果为：{reality}  # 现在显示的是文本，而不是对象
        断言结果：{expected} != {reality}'''


    # 验证码处理
    def get_code(self, by, value):
        file = self.locator(by, value).screenshot_as_png
        return ddddocr.DdddOcr(show_ad=False).classification(file)