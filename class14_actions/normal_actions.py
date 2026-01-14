'''
    Selenium中常见的操作：
        1. 操作行为分为浏览器操作和元素操作。基本上所有的操作行为都属于这两大类
            【浏览器操作行为】是针对浏览器本身；
            【元素操作行为】是针对已获取的元素对象来执行。
        2. 元素操作的行为都是基于已经获取到元素之后才可以进行的。
'''

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=service)

# 常规操作行为
# 常规操作行为
# 常规操作行为

# 浏览器最大化
driver.maximize_window()    # 属于一个操作步骤，会有明显的浏览器大小变化。如果要使用，一般是放在最开始的位置。
# time.sleep(2)

# 设置浏览器尺寸
# driver.set_window_size(400, 800)    # 没必要和浏览器最大化一起使用
# time.sleep(2)

# 访问URL
driver.get('https://www.baidu.com') # URL一定要完整的内容，缺少前缀则无法识别，代码会报错。

"""
获取浏览器title信息。一般在调试的时候使用的更多
"""
print(driver.title)


"""
元素操作都是在find_element之后进行的。
元素的输入：send_keys。该方法只能应用于input标签。
"""
# driver.find_element('id', 'chat-textarea').send_keys('schillernd')

"""
元素的文件上传：send_keys，本质上是一个输入操作，但【只能对input标签实现文件的上传】（大部分的文件上传是通过input完成的）。
上传文件时，需要传入文件的完整路径、文件名和后缀名
"""
# driver.find_element('xpath', '//*[@class="tool-item_1e6GD "]').send_keys(r'C:\Users\1\Desktop\SystemInformation.txt')
# time.sleep(3)


"""
元素的点击：click。实现对元素进行单击操作行为。
"""
# driver.find_element().click()


"""
鼠标悬停：ActionChains类可以帮助我们实现悬停操作。
操作过程中记得不要移动鼠标
.perform()：执行所有存储的actions
"""
ActionChains(driver).move_to_element(driver.find_element('xpath', '//*[@id="s-usersetting-top"]')).perform()
driver.find_element('link text', '高级搜索').click()



"""
下拉列表框的操作：推荐的方式是两次click来实现下拉列表框的值的选择。
    第一次：点击下拉列表框
    第二次：点击下拉列表框的值
"""
time.sleep(2)
driver.find_element('xpath', '//*[@class="c-select-selected-value"]').click()
driver.find_element('xpath', '//p[text()="一年内"]').click()

"""
select下拉列表框的操作.有三种方法：by_index、by_value、by_visible_text
Select标签的下拉列表框选择（技术相对老旧，一般少见。）
            <select id="hcc" name="123">
                <option selected="true;" value="17">财财</option>
                <option value=""> 新地址 </option>
            </select>
"""
select = Select(driver.find_element('id', 'hcc'))
select.select_by_index(1)  # 基于选项的下标选择。默认从1开始，也就是财财选项
select.select_by_value("17")  # 基于选项的value属性进行选择。也就是财财选项
select.select_by_visible_text("新地址")  # 基于选项的文本进行选择，也就是新地址选项





"""
浏览器的关闭：
    Selenium默认在程序结束时会调用driver.quit()实现资源的释放。但还是建议在程序末尾手动添加quit()方法
"""
# driver.close()  # 关闭当前标签页
# 关闭指定的标签页:

driver.quit()  # 关闭整个浏览器并释放资源，结束当前driver生命周期。

# 当调用quit之后，driver对象无法再继续使用，因为已经结束了。如果还需要调用driver，则需要新建一个新的driver对象再继续操作。

time.sleep(5)