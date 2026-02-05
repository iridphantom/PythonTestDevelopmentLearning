"""
    ERP的测试流程：测试用例层级，用于管理测试用例和编写测试代码。
"""
import unittest

from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

from class17_options.options import firefox_options

from class23_pom.page_object.login_page import LoginPage
from class23_pom.page_object.add_vendor_page import AddVendorPage
from class23_pom.page_object.logout import Logout


@ddt
class TestErp(unittest.TestCase):
    """
        类级前后置处理setUpClass、tearDownClass
        在整个测试类开始和结束时调用，只执行一次。
        要使用@classmethod
    """
    @classmethod
    def setUpClass(cls):    # 创建driver对象。整个测试类只会执行一次 setUpClass，避免了多次启动浏览器。
        print('所有测试用例执行前的初始化操作')

        service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\geckodriver.exe")
        cls.driver = webdriver.Firefox(service=service, options=firefox_options())

        # driver生成好后，就可以进行页面对象实例化
        cls.login_page = LoginPage(cls.driver)
        # 实现业务的关联：登录后-->添加供应商。
        # 以后要关联多少个页面对象，就在这后面接着初始化（实例化）
        cls.add_vendor_page = AddVendorPage(cls.driver)
        cls.logout = Logout(cls.driver) # 提前初始化 logout对象，确保类级后置处理能够调用


    @classmethod
    def tearDownClass(cls):
        print('所有测试用例执行后的收尾操作')
        # cls.logout.logout()  # 直接调用已初始化的 logout 对象.(这里要使用的话，就要先在setUpClass中初始化)
        cls.driver.quit()   # 退出浏览器


    @file_data('../test_data/login.yaml')   # 类的上面记得要加@ddt
    def test_01_login(self, username, password):
        self.login_page.login(username, password)
    """
            在上面这段代码中，self 指的是当前测试类 TestErp 的实例对象。具体来说：
                self 是 Python 中实例方法的第一个参数，用于引用调用该方法的具体实例。
                在 test_01_login 方法中，self 代表 TestErp 类的一个实例，通过它可以访问该实例的属性和方法。
            例如：
                self.login_page：访问实例中初始化的 LoginPage 页面对象。
                self.login_page.login(username, password)：调用 LoginPage 对象的 login 方法，执行登录操作。
            总结：self 在这里是 TestErp 类实例的引用，用于操作实例级别的属性和方法。
        """

    @file_data('../test_data/vendor.yaml')
    def test_02_add_vendor(self, vendor_name, vendor_email):
        self.add_vendor_page.add_vendor(vendor_name, vendor_email)

    def test_03_logout(self):
        self.logout.logout()


if __name__ == '__main__':
    unittest.main()