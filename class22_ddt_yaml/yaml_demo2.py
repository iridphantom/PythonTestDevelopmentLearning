# test_with_ddt.py
import unittest
from ddt import ddt, data, unpack
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path


def load_yaml_data(filepath):
    """加载 YAML 测试数据"""
    file_path = Path(filepath)
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


@ddt
class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """测试类初始化"""
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        """测试类清理"""
        cls.driver.quit()

    def setUp(self):
        """每个测试前的设置"""
        pass

    @data(*load_yaml_data('test_data.yaml'))
    def test_search_functionality(self, test_case):
        """测试搜索功能 - 使用数组数据"""
        # 执行测试
        self.driver.get(test_case['url'])

        # 根据 URL 选择不同的搜索框定位器
        if 'baidu.com' in test_case['url']:
            search_box_locator = (By.ID, "kw")  # 百度搜索框ID
            search_button_locator = (By.ID, "su")  # 百度搜索按钮ID
        elif 'google.com' in test_case['url']:
            search_box_locator = (By.NAME, "q")  # Google搜索框NAME
            search_button_locator = (By.NAME, "btnK")  # Google搜索按钮NAME

        # 输入搜索关键词
        search_box = self.wait.until(
            EC.presence_of_element_located(search_box_locator)
        )
        search_box.clear()
        search_box.send_keys(test_case['search_term'])

        # 点击搜索按钮
        search_button = self.driver.find_element(*search_button_locator)
        search_button.click()

        # 验证搜索结果（这里简化为检查页面标题包含关键词）
        self.wait.until(EC.title_contains(test_case['search_term']))

        # 断言
        self.assertIn(test_case['search_term'], self.driver.title)
        print(f"测试通过: {test_case['name']}")


@ddt
class TestUserAuthentication(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, 10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*load_yaml_data('user_data.yaml'))
    def test_user_login(self, user_data):
        """测试用户登录 - 使用映射数据"""
        # 这里假设我们有一个登录页面
        # self.driver.get("https://example.com/login")

        # 实际测试中需要替换为真实的登录页面和元素定位器
        print(f"测试用户: {user_data['username']}, 角色: {user_data['role']}")
        print(f"期望登录结果: {user_data['expected_login']}")

        # 模拟登录过程
        # username_input = self.driver.find_element(By.ID, "username")
        # password_input = self.driver.find_element(By.ID, "password")
        # login_button = self.driver.find_element(By.ID, "login")
        #
        # username_input.send_keys(user_data['username'])
        # password_input.send_keys(user_data['password'])
        # login_button.click()
        #
        # # 验证登录结果
        # actual_result = "dashboard" in self.driver.current_url
        # self.assertEqual(actual_result, user_data['expected_login'])


@ddt
class TestMultipleParameters(unittest.TestCase):
    """测试多参数传递"""

    def setUp(self):
        self.test_data = [
            ["python", "programming", "language"],
            ["selenium", "automation", "testing"],
            ["yaml", "configuration", "format"]
        ]

    @data(*load_yaml_data('test_data.yaml'))
    def test_multiple_params(self, test_case):
        """测试多个参数"""
        print(f"测试名称: {test_case['name']}")
        print(f"URL: {test_case['url']}")
        print(f"搜索词: {test_case['search_term']}")
        print(f"预期结果: {test_case['expected_result']}")
        print(f"超时时间: {test_case['timeout']}")

        # 这里可以执行实际的测试逻辑
        self.assertIsNotNone(test_case['name'])
        self.assertIsNotNone(test_case['url'])
        self.assertIsNotNone(test_case['search_term'])


@ddt
class TestWithCustomIds(unittest.TestCase):
    """测试自定义测试ID"""

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def id_generator(test_case):
        """自定义测试ID生成器"""
        return f"{test_case['name'].replace(' ', '_')}"

    @data(*load_yaml_data('test_data.yaml'))
    @unpack
    def test_with_custom_ids(self, test_case):
        """使用自定义ID的测试"""
        print(f"执行测试: {test_case['name']}")
        # 实际测试逻辑
        self.assertIsNotNone(test_case['url'])


# 另一种使用方式：直接在装饰器中加载数据
@ddt
class TestDirectLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 直接在装饰器中加载数据（但要注意文件路径问题）
    @data(
        *yaml.safe_load(Path('test_data.yaml').read_text(encoding='utf-8'))
    )
    def test_direct_load(self, test_case):
        """直接加载数据的测试"""
        print(f"测试: {test_case['name']}")
        self.assertIn('url', test_case)
        self.assertIn('search_term', test_case)


if __name__ == '__main__':
    unittest.main(verbosity=2)