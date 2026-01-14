'''
    浏览器操作行为：
        1. 自动生成新的浏览器或者标签页
                Selenium默认情况下创建的浏览器是带有数据隔离的，也就是沙箱功能。（第一个浏览器登录百度后，再打开一个浏览器，第二个浏览器是没有登录的）
            主要用于解决多用户业务流程的自动化执行。
        2. 注意事项：
            1. 必须是Selenium4+的版本才支持该方法。
            2. python版本必须在3.10+才支持
            3. 不管是new window还是new tab，都可以通过句柄来控制。
            4. 生产新的tab或者window后，句柄会自动切换到新的对象。
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# 打开百度，也就是创建第一个浏览器
driver.get('https://www.baidu.com')

# 创建一个新的浏览器或者标签页。通过参数type hint来实现，tab表示标签页，window表示浏览器，自动切换句柄到新生成的标签页或者浏览器
driver.switch_to.new_window('tab')  # 创建一个新的标签页
# driver.switch_to.new_window('window')  # 创建一个新的浏览器

driver.get('http://www.jd.com')

time.sleep(5)