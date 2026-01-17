"""
    用例文件的定义和管理：
        基于erp系统实现客户记录的新增与删除功能
    整个实操案例：
            1. 登录erp系统
            2. 获取客户信息
            3. 新增一条客户记录
            4. 修改/删除新增的客户记录信息
            5. 断言校验流程的正确性。
    用例的设计：
        1. 拆分子流程
        2. 封装不同的子流程
        3. 进行最终业务结果的断言校验
        4. 考虑前置与后置条件的相关应用

    1. 前置条件和后置条件不参与任何的操作行为。
    2. 子流程业务必须完整，且前面的子流程可以不断言，可以断言。根据你的需要。
    3. 每一个用例之间一定要尽可能地低耦合状态。彼此之间最好要不关联。
"""
import unittest
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from class18_web_keys.web_keys import WebKeys

text = 'UnitTest自动化新增数据变量6'
telephone = '123456'
email = '123@qq.com'

class TestAdd(unittest.TestCase):
    # 定义【类级】前置条件
    @classmethod
    def setUpClass(cls):
        cls.driver = WebKeys('FireFox')  # 初始化浏览器对象

    # 定义【类级】后置条件
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_01_login(self):    # 注意命名方式。
        self.driver.open("http://39.101.122.147:3000/user/login")
        # self.driver.input('id', 'loginName', 'jsh')
        # self.driver.input('id', 'password', '123456')
        code = self.driver.get_code('xpath', '//img[@data-v-4f5798c5]') # 获取验证码
        self.driver.input('id', 'inputCode', code)  # 输入验证码
        self.driver.click('xpath', '//button[@data-v-4f5798c5]')    # 点击登录
        sleep(2)

    def test_02_userInfoPage(self): # 跳转到用户信息页面
        self.driver.click('xpath', '//span[text()="基本资料"]')
        sleep(1)
        self.driver.click('xpath', '//a[@target="客户信息"]')
        sleep(1)

    def test_03_addUser(self):
        self.driver.click('xpath', '//span[text()="新增"]/..')
        sleep(1)
        self.driver.input('id', 'supplier', text)
        self.driver.input('id', 'telephone', telephone)
        self.driver.click('xpath', '//span[text()="保 存"]/..')
        sleep(1)

    def test_04_modify(self):   # 修改
        self.driver.click('xpath', f'//td[text()="{text}"]/../td[3]/span/a[1]') # 点击编辑
        self.driver.input('id', 'email', email)  # 添加邮箱
        self.driver.click('xpath', '//span[text()="保 存"]/..')
        sleep(1)

    def test_05_assert(self):
        # 断言：判断修改是否成功添加邮箱：
        saved_email = WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.locator('xpath', f'//td[text()="{email}"]/..//td[8]')
        ).text

        print(f"获取到保存的邮箱为：{saved_email}")

        self.assertEqual(email, saved_email, f"邮箱保存失败，期望值: {email}, 实际值: {saved_email}")
        sleep(1)


    def test_06_logout(self):
        sleep(1)
        self.driver.click('xpath', '//a[@class="logout_title"]')
        sleep(1)
        self.driver.click('xpath', '//span[text()="确 定"]/..')
        sleep(1)

        # 判断是否成功退出登录
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda element: self.driver.locator('xpath', '//small[text()="V3.3"]'),
            message='退出登录失败')  # 创建一个显式等待对象, 10秒内每隔0.5秒检查一次目标元素是否加载完成, 如果超过10秒还没有加载完成，就会抛出异常。

        sleep(5)

if __name__ == '__main__':
    unittest.main()