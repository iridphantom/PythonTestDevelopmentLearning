'''
    三类等待：
        为了让程序可以稳定运行。所以需要有合理的等待机制让程序具备有更好的稳定性。
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.baidu.com')
driver.find_element('id', 'chat-textarea').send_keys('schillernd')
driver.find_element("xpath", '//*[@id="chat-submit-button"]').click()

"""
    隐式等待：一般都是在创建driver对象之后，就设置。
"""
driver.implicitly_wait(5)   # 设置隐式等待时间，5秒内如果页面没有加载完成，就会等待5秒，如果页面加载完成，就会继续执行。


"""
    显式等待
"""
el = WebDriverWait(driver, 10, 0.5).until(
    lambda element: driver.find_element('xpath', '//*[@id="1"]/div/h3/a12'),
    message='元素获取失败')  # 创建一个显式等待对象, 10秒内每隔0.5秒检查一次目标元素是否加载完成, 如果超过10秒还没有加载完成，就会抛出异常。
# driver.find_element('xpath', '//*[@id="1"]/div/h3/a12') 会返回一个对象
el.click()

# until_not：如果需要等待某个气泡或者弹层消失之后再继续操作，则可以调用此类方法。
# WebDriverWait(driver, 5, 0.5).until_not(
#     lambda element: driver.find_element('xpath', '//*[@id="1"]/div/h3/a'),
#     message='元素获取失败'
# )
# driver.find_element('xpath', '//*[@id="1"]/div/h3/a12') 不会返回对象


time.sleep(5)   # 强制等待
driver.quit()