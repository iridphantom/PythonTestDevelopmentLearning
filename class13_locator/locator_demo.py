'''
八大元素定位法则：
    所有的元素定位，都基于一个核心方法，就是driver.find_element()

    当获取到多个重复元素时，默认find_element()方法会返回获取的第一个元素。
    在定位元素的时候，一定要尽可能保障使用的定位方法能够获取唯一元素，避免多个元素满足条件。
    元素定位方法获取的都是WebElement对象，也就是元素对象。

    虽然可以直接复制xpath或者css selector，但一般不会直接复制。因为稳定性存疑。
    
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.baidu.com")

# id：基于元素的id属性进行定位。必须要求元素具备id属性，正常情况下id是唯一的。不同元素的id一般不同
# id="chat-textarea"
driver.find_element('id', 'chat-textarea')

# name：基于元素的name属性来进行定位。必须要求元素具备name属性。但是name可能会有重名，需要自行判断。
# name="tj_briicon"
driver.find_element('name', 'tj_briicon')

# tagname：基于元素的标签名称来定位。不推荐在自动化使用。一般用于爬虫
driver.find_elements('tag name', 'input')   # find_elements返回list内容。

# classname：基于元素的class属性，实现元素的定位。不推荐
# class="chat-input-textarea chat-input-scroll-style"
# 一个class可以有多个class值
driver.find_element('class name','')

# link text：只能用于a标签。通过元素的文本来实现元素定位。
driver.find_element('link text', '新闻')

# partial link text 只能用于a标签。基于元素的文本进行模糊查找。
driver.find_element('link text', '新')   # 只要带有“新”的，都会去寻找

# CSS Selector / CSS选择器：被称之为定位界的万金油之一，是定位效率最快的方法（运行时间）。
# 有自己的语法结构
driver.find_element('css selector', '#chat-textarea')

# XPath：也是定位界的万金油之一。基于路径的方式获取指定元素，有自己的语法结构
driver.find_element('xpath', '//*[@id="chat-textarea"]')



time.sleep(5)