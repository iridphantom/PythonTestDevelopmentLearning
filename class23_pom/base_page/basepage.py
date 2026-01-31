"""
    BasePage类：用于实现Selenium的操作行为封装
"""
import time
import ddddocr

class BasePage:

    """
        如何判断什么时候需要编写构造方法？
         1. 需要初始化实例属性：
            如果类中的某些属性需要在创建对象时就被赋予初始值（例如数据库连接、配置参数、驱动对象等），就需要使用构造方法来完成这些初始化工作。
         2. 需要执行初始化逻辑：
            如果类在创建对象时需要执行一些特定的操作（例如打开文件、建立网络连接、设置默认状态等），可以通过构造方法来实现。
         3. 依赖外部参数：
            如果类的功能依赖于外部传入的数据或对象（如这里的 driver 参数），则必须通过构造方法接收这些参数，并将其绑定到实例上。
         4. 统一资源管理：
            构造方法可以帮助统一管理和分配资源，避免每次使用类时都需要手动设置关键属性或执行重复的初始化步骤。

        因此，在设计类时，只要涉及实例属性的初始化、依赖注入或前置逻辑处理，就应该考虑编写构造方法。
    """

    # 构造方法
    def __init__(self, driver): # 这个构造方法的作用：初始化驱动对象、设置隐式等待时间
        self.driver = driver  # 确保每一个完整流程都是基于同一个driver对象来实现的。
        self.driver.implicitly_wait(5)

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

    # 验证码处理
    def get_code(self, by, value):
        file = self.locator(by, value).screenshot_as_png
        return ddddocr.DdddOcr(show_ad=False).classification(file)