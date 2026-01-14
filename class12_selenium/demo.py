import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 初始化浏览器，指定本地驱动
# 配置service，创建了一个ChromeDriver服务实例
service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")

"""
自动解决浏览器依赖：自动下载对应版本的Driver到缓存目录中
driver = webdriver.Chrome(ChromeDriverManager().install())
"""

# 启动浏览器，创建一个driver对象，需要将配置传入driver对象，便于调用本地driver启动浏览器
driver = webdriver.Chrome(service=service)

# 访问baidu.com
driver.get("https://www.baidu.com")

# 最大化浏览器
driver.maximize_window()
time.sleep(2)
"""
# 获取浏览器尺寸，打印在控制台
# print(driver.get_window_size())

# 设置浏览器尺寸
# driver.set_window_size(width=1000, height=1000)

# 获取浏览器位置
# print(driver.get_window_position())

# 设置浏览器位置
# driver.set_window_position(x=100, y=100)
"""

# 输入搜索内容
input_element = driver.find_element("id", "chat-textarea")
input_element.send_keys("SAD")

time.sleep(2)

# 按下搜索按钮 byId:
# baidu_button = driver.find_element("id", "chat-submit-button")
# ByXPath：
baidu_button = driver.find_element("xpath", '//*[@id="chat-submit-button"]')
baidu_button.click()
time.sleep(2)

time.sleep(10)
# 关闭所有标签 / 窗口
driver.quit()