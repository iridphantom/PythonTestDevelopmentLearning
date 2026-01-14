'''
    基于关键字驱动类封装的关键字实现自动化测试效果。属于测试代码
    测试代码其实就是人类按照系统业务流程，进行的流程操作步骤。从而实现自动运行的效果。
    说白了就是测试代码是测试用例。
'''
from class18_web_keys.web_keys import WebKeys

# 实例化关键字类，进行自动化操作。其中的数据可以通过数据驱动导入，例如CSV、Excel，具体看下一节课的代码。
driver = WebKeys('Chrome')  # 告诉系统使用Chrome浏览器
driver.open("https://www.baidu.com")

driver.input('id', 'chat-textarea', 'schillernd')
driver.click('xpath', '//*[@id="chat-submit-button"]')

driver.wait(20)
driver.assert_text('xpath', '//*[text()="实际结果"]', '预期结果')
driver.quit()

