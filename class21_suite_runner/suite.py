"""
    测试套件
        1. 单独新建一个py文件，用于编写套件代码的相关逻辑。
        2. 套件就是用于添加测试用例的。执行套件其实也就是执行添加的指定套件中的所有测试用例。
        3. 套件的运行必须关联运行器
        4. 添加套件的测试用例，在执行时，不会遵循UnitTest的排序规则
"""

import datetime
import os
import unittest
import HTMLTestRunner_cn

from class21_suite_runner.test_class21_demo01 import TestDemo01, TestDemo02

# 套件添加测试用例的示例
# 创建套件
suite = unittest.TestSuite()  # 相当于创建了一个空的list

# 添加测试用例
"""
    添加测试用例方法1：基于测试用例的名称来添加
"""
# suite.addTest(TestDemo01('test_demo03'))  # 添加TestDemo类下的test_demo03测试用例至套件之中
# suite.addTest(TestDemo01('test_demo02'))
# suite.addTest(TestDemo01('test_demo01'))


"""
    方法2：批量实现对用例的添加
"""
# cases = [TestDemo01('test_demo03'), TestDemo01('test_demo02'), TestDemo01('test_demo01'), TestDemo02('test_01')]    # 本质上还是基于用例名称来实现用例的添加
# suite.addTests(cases)   # 注意是复数，有s


"""
    方法3：基于class来实现对用例的添加。
    用例的执行顺序还是遵循UnitTest的默认顺序
"""
# cases = [
#     unittest.TestLoader().loadTestsFromTestCase(TestDemo01),
#     unittest.TestLoader().loadTestsFromTestCase(TestDemo02)
# ]   # 添加TestDemo01、TestDemo02类下的所有测试用例至套件之中。（添加到list中）
# suite.addTests(cases)  #  # 注意是复数，有s


"""
    方法4：基于py文件添加测试用例
"""
# cases = ['test_class21_demo01', 'test_class21_demo02']  # 基于文件名称，生成list。默认会读取整个py文件所有的class
# suite.addTests(unittest.TestLoader().loadTestsFromNames(cases)) #


"""
    方法5：基于discover添加测试用例。（推荐）
"""
path = './'  # 用例获取的路径
discover = unittest.defaultTestLoader.discover(start_dir=path,  # 指定测试用例的目录
                                               pattern='test_*.py'  # 用例匹配规则。更加灵活，可以指定获取哪些py文件 / 用例
                                               )  # 默认返回一个测试套件

# 套件的运行：需要基于运行器来实现。
# runner = unittest.TextTestRunner(verbosity=2)  # 默认运行器。运行时，会按照测试用例添加的顺序执行。会在控制台中显示执行结果。
# verbosity=2：显示详细执行结果
# 方法1-4：
# runner.run(suite)   # 基于运行器执行测试套件

# 方法5：
# runner.run(discover)


"""
    由于上面的runner.run(suite)或者runner.run(discover)的测试结果都打印在控制台中，可以通过引入测试报告，更直观的展示执行结果
    第三方测试报告，本质上也就是一个运行器。用来执行测试套件的。
    测试报告配置
"""
# 测试报告配置：
report_dir = './report/'  # 测试报告保存路径
# report_time = '{0:%Y-%m-%d %H_%M_%S}'.format(datetime.datetime.now())
report_time = '{0:%Y-%m-%d %H_%M_%S_%f}'.format(datetime.datetime.now())  # 精确到毫秒
report_file = report_dir + report_time + 'report.html'
tester = 'iridescent'

# 判断测试报告保存路径是否存在
if not os.path.exists(report_dir):
    os.mkdir(report_dir)

# 测试报告生成
with open(report_file, 'wb') as file:
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='测试报告',
                                              description='测试结果如下：')
    runner.run(discover)

"""
    1. 如果想要实现更深层次的用例管理，一定会关联到套件的应用。
    2. 一般而言套件和测试报告的使用，我们会提前封装成函数的形态来执行，也可以关联邮件自动发送或者第三方办公软件的api接入。
    3. 测试报告的命名和管理一般是基于时间戳来实现的。
        如果一次性执行10个测试用例文件文件，但没有生成10份测试报告。主要原因是时间戳不够精准，生成的测试报告被覆盖了，为了避免这种情况，时间戳最好精确到毫秒级
        但是，如果你是基于多线程来实现不同套件的并发用例效果。时间戳一定要精确到最少毫秒级别
"""
