"""
    退出登录
"""

from class23_pom.base_page.basepage import BasePage

class Logout(BasePage):

    logout_button = ('xpath', '//a[@class="logout_title"]')   # “退出登录”按钮
    confirm_button = ('xpath', '//span[text()="确 定"]/..')    # “确定”按钮

    def logout(self):
        self.click(*self.logout_button)
        self.click(*self.confirm_button)
        self.wait(3)