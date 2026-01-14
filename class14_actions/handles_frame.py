'''
    handles：句柄。标签页
        自动化测试执行中，我们获取的都是当前页面下的元素来进行的操作。而当前页面，是基于句柄来控制的。
        每一个标签页都有属于自己的句柄。句柄无法自动切换。就算页面显示的是新的标签页，但Selenium的句柄还是
        停留在最初始的第一个标签页。如果要操作新的标签页，则需要手动切换句柄到指定标签页才可以继续后续的操作。
        否则新标签页中的内容是无法被获取和操作的。

        切换句柄页操作：
            1. 获取所有句柄
            2. 切换到指定句柄
        句柄的保存建议各位最多不超过两个，一旦句柄太多则操作会产生不必要的麻烦。记得通过close关闭不必要的句柄页。
'''

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get('https://www.baidu.com')
driver.find_element('id', 'chat-textarea').send_keys('schillernd')
driver.find_element("xpath", '//*[@id="chat-submit-button"]').click()
time.sleep(2)
driver.find_element('xpath', '//*[@id="4"]/div[1]/div[1]/div[1]/div[1]/div[1]/h3[1]/a').click()

# 切换句柄
handles = driver.window_handles # 获取当前所有句柄。handles是list，也就是列表
# driver.close()  # 关闭旧的标签页，但此时句柄还是有两个值。一个是关闭的旧标签页的值，另一个是新标签页的值
driver.switch_to.window(handles[1])  # 切换到新的句柄页
time.sleep(5)

# 操作新的标签页元素
driver.find_element('xpath', '//*[@id="main-nav"]/ul/li[4]/a').click()




"""
    frame窗体：是内嵌窗体，相当于在原有的HTML页面中，内嵌了一个独立的HTML页面。frame中的元素无法被直接访问和操作。
    如果想要访问frame中的元素，则需要先切换至frame之中，再操作该元素。
    注意：切换进入frame之后，frame以外的元素则无法操作，需要切换出来才可以继续操作frame以外的元素。
    
    如何判断是否是frame窗体：找<iframe>标签
        
"""
driver.get('https://wx.mail.qq.com/')
# 进入第一层iframe
driver.switch_to.frame(driver.find_element('xpath', '//div[@id="QQMailSdkTool_login_loginBox_qq"]/iframe'))

# 进入第二层iframe
driver.switch_to.frame(driver.find_element('id', 'ptlogin_iframe'))
driver.find_element('link text', '密码登录').click()

# 如果要操作iframe以外的元素，则需要先切换至默认窗体
driver.switch_to.default_content()  # 切换至默认窗体的操作方法。
driver.find_element('link text', '基本版').click()


time.sleep(5)
driver.quit()