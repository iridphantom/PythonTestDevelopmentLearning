'''
    document对象操作：（了解，使用频率很低）
        1. getElementById()，通过id获取到指定元素的定位方法。（获取到的是单个元素）
        2. setAttribute(属性,值)，设置指定元素的属性值，如果属性不存在，则为新增属性，如果属性存在，则为修改属性值
        3. removeAttribute(属性)，将指定元素的指定属性删除。
        4. innerHTML="值"，为指定元素进行文本的添加，若元素本身已有文本，则为修改文本内容。并将文本值返回

    js操作滚动条：已弃用。因为有更好的更简单的选择————通过ActionChains类来实现。
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(r'D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.baidu.com')

