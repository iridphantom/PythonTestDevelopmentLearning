"""
    添加供应商信息
"""
from class23_pom.base_page.basepage import BasePage


class AddVendorPage(BasePage):
    url = 'http://39.101.122.147:3000/system/vendor'


    # 需要操作的核心元素
    add_vendor_button = ('xpath', '//div[@class="table-operator"]/button[1]')   # “添加”按钮
    vendor_name_input = ('xpath', '//input[@id="supplier"]')    # 供应商名称输入框
    vendor_email_input = ('xpath', '//input[@id="email"]')      # 供应商邮箱输入框
    vendor_save_button = ('xpath', '//span[text()="保 存"]/..')   # 保存按钮


    def add_vendor(self, vendor_name, vendor_email):
        self.open(self.url)
        self.wait(1)
        self.click(*self.add_vendor_button)
        self.input(*self.vendor_name_input, txt=vendor_name)
        self.input(*self.vendor_email_input, txt=vendor_email)
        self.click(*self.vendor_save_button)
        self.wait(5)


    # search_name = ('xpath', '//input[@placeholder="请输入名称查询"]')
    # search_button = ('xpath', '//span[text()="查 询"]/..')
    #
    # def vendor_search(self, vendor_name):
    #     self.open(self.url)
    #     self.input(*self.search_name, txt=vendor_name)
    #     self.click(*self.search_button)