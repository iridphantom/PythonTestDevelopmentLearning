'''
    页面加载策略的修改：自动化测试执行的提升效率的手段之一。但是使用此方法需要慎重，因为可能会产生未知的风险。
        Selenium总计有三种不同的页面加载策略：
            1. normal：默认加载策略，所有内容全部加载完后才会继续后续的代码执行
            2. eager：只加载基本的dom树，不考虑任何静态资源
            3. none： 值加载基本的页面结构，不考虑其他任何东西
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


"""
    页面加载策略的修改
    创建浏览器设置对象
"""
options = webdriver.ChromeOptions()  # 你是什么浏览器就创建什么类型的options对象
# 设置页面加载策略，默认是normal
# options.page_load_strategy = 'eager'  # 设置为eager等级
# options.page_load_strategy = 'none'    # 设置为none等级

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)  # 如果要让设置生效，记得传入options对象作为参数
driver.maximize_window()

driver.get('https://www.baidu.com')
driver.find_element('id', 'chat-textarea').send_keys('schillernd')
driver.find_element("xpath", '//*[@id="chat-submit-button"]').click()


time.sleep(5)
driver.quit()