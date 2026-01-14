'''
    网站：http://39.101.122.147:3000/user/login
        账号：jsh
        密码：123456

    WebUI实操案例讲解：
        基于已经学习的所有自动化内容，实现对网站的UI自动化测试实操演示
        1. 请注意我在实现代码的时候，我的思路。不要只看我写的代码。
        2. 全程基于erp系统来实现自动化实操，会关联到验证码的处理问题。所以会额外教大家一个库的应用。
        3. 整个实操案例：
            1. 登录erp系统
            2. 获取客户信息
            3. 新增一条客户记录
            4. 修改/删除新增的客户记录信息
            5. 断言校验流程的正确性。

    考虑到加载本地缓存，会出现有时不需要登录的情况。
        1. 将登录流程用try except括起来。如果报错。直接进入到新增的流程之中。
        2. 在业务执行结束时，进行登出操作
'''
import time
import ddddocr

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

# Firefox个人资料路径
profile_path = r"C:\Users\1\AppData\Roaming\Mozilla\Firefox\Profiles\vby4egfz.default-release"

# 测试数据：账号密码
user = 'jsh'
pwd = '123456'

options = webdriver.FirefoxOptions()
# options.add_argument('start-maximized')
options.add_argument("-profile")
options.add_argument(profile_path)


# driver初始化：因为ERP第一次加载速度慢，所以建议添加本地缓存，提升加载速度
service = Service(r"D:\DevelopmentEnvironment\BrowserDrivers\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=options)
driver.implicitly_wait(5)

# 访问URL
driver.get("http://39.101.122.147:3000/user/login")

# 执行登录操作
# driver.find_element('id', 'loginName').send_keys(user)
# driver.find_element('id', 'password').send_keys(pwd)

"""
    验证码一般不自动化处理。如果必须要处理，绕不开，一般可以使用ddddocr库来实现。它基于图片来进行内容识别，自动解析生成验证码内容。
    所有验证码处理都是一样的方式：
        获取验证码图片，解析图片内容，获取值，校验是否正确，如果错误，则刷新验证码图片。重头再来一次。
        while true:
            获取验证码
            解析验证码
            点击确认
            if 校验成功
                break
            else:
                pass
    验证码如果是很复杂的内容，则不推荐自行解决。因为成功率太低。
"""
# 基于ddddocr实现验证码的处理
file = driver.find_element('xpath', '//img[@data-v-4f5798c5]').screenshot_as_png  # 获取验证码图片：截图，保存为PNG文件
driver.find_element('id', 'inputCode').send_keys(ddddocr.DdddOcr(show_ad=False).classification(file))   # 将验证码图片内容解析成文字信息。show_ad=False避免打印广告

time.sleep(2)

# 点击登录按钮
driver.find_element('xpath', '//button[@data-v-4f5798c5]').click()

time.sleep(2)

# 进入基本资料页
driver.find_element('xpath', '//span[text()="基本资料"]').click()
time.sleep(2)
# 进入客户信息页
driver.find_element('xpath', '//a[@target="客户信息"]').click()
time.sleep(2)
# 新增客户信息
driver.find_element('xpath', '//span[text()="新增"]/..').click()
time.sleep(2)

# 关键数据提取变量，方便代码的维护管理。数据可以选择随机生成，方便多次运行时查看结果
text = '自动化新增数据变量3'
telephone = '123456'
driver.find_element('id', 'supplier').send_keys(text)
driver.find_element('id', 'telephone').send_keys(telephone)
driver.find_element('xpath', '//span[text()="保 存"]/..').click()

time.sleep(2)

# 删除新增的数据
driver.find_element('xpath', f'//td[text()="{text}"]/../td[3]/span/a[2]').click()  # 点击删除按钮：根据text，定位到'自动化新增数据变量'的位置，然后根据xpath定位到该元素的删除按钮
time.sleep(2)
driver.find_element('xpath', '//span[text()="确 定"]/..').click() # 点击确定

time.sleep(2)

# 断言校验：如果是删除，可以通过until not来断言。
# until_not：如果需要等待某个气泡或者弹层消失之后再继续操作，则可以调用此类方法。
WebDriverWait(driver, 5, 0.5).until_not(
    lambda element: driver.find_element('xpath', f'//td[text()="{text}"]'),
    message='删除失败，请检查'
)

# 点击退出登录，并确定退出登录
driver.find_element('xpath', '//a[@class="logout_title"]')
driver.find_element('xpath', '//span[text()="确 定"]/..')

print("操作成功")

time.sleep(5)
driver.quit()