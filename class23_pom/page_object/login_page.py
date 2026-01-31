"""
    实现ERP的登录操作行为

    获取页面元素（与操作流程相关联的） -->

    每一个页面对象的代码结构模板都是相同的。可以直接复制，然后稍作修改。
"""
import ddddocr

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from class23_pom.base_page.basepage import BasePage

class LoginPage(BasePage):    # 让LoginPage继承BasePage，就可以调用BasePage中的方法
    # 页面URL
    url = 'http://39.101.122.147:3000/user/login'

    # 页面核心元素(需要操作的核心元素)
    # 元素核心内容包括定位方法、对应的value值
    login_input_username = ('id', 'loginName')  # 获取用户名输入框的元素定位信息
    login_input_password = ('id', 'password')
    login_input_code = ('id', 'inputCode')
    login_code_img = ('xpath', '//img[@data-v-4f5798c5]')   # 获取验证码图片的元素定位信息
    login_button = ('xpath','//button[@data-v-4f5798c5]')



    # 页面的子流程封装
    def login(self, username, password):
        self.open(self.url)
        #self.input(*self.login_input_username, txt= username)  # *：解元组。   由于浏览器已导入缓存，会自动填充，这里就不输入了
        #self.input(*self.login_input_password, txt= password)
        self.input(*self.login_input_code, txt=self.get_code(*self.login_code_img))
        self.click(*self.login_button)
        self.wait(5)


# 编写完后，可以先运行一下，查看是否正常。
# if __name__ == '__main__':
#     service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\geckodriver.exe")
#
#     # 添加firefox本地缓存和一些配置，提升页面打开速度
#     options = webdriver.FirefoxOptions()
#     profile_path = r"C:\Users\1\AppData\Roaming\Mozilla\Firefox\Profiles\vby4egfz.default-release"  # Firefox个人资料路径
#     options.add_argument('start-maximized')
#     options.add_argument("-profile")
#     options.add_argument(profile_path)
#
#     driver = webdriver.Firefox(service=service, options=options)
#     lp = LoginPage(driver)
#     lp.login('jsh', '123456')