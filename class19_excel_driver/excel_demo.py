'''
    openpyxl的基本应用
        1. excel文件操作：
            创建 / 打开excel文件
            找到对应的sheet页
            找到对应的cell
            对cell金编辑或者读取
        2. 可以实现对文件的读取和写入，包括excel的各类样式的配置

    不要在pycharm中直接创建excel文件，否则会出现文件损坏的情况。
'''

import openpyxl

"""
Openpyxl示例
"""

"""
读取excel中的内容
"""
# 1. 找到excel文件:
excel = openpyxl.load_workbook('./demo.xlsx')
# 找到对应的sheet页
sheet1 = excel['Sheet1'] # 获取sheet页是以字典的方式来获取的。
# 获取对应单元格的内容
# print(sheet['A1'].value)    # 读取A1单元格中的内容
# print(sheet['C4'].value)    # 读取C4单元格中的内容

# print("-" * 50)

# 获取整个sheet页的单元格内容
for value in sheet1.values:
    print(value)    # 打印每一行的内容，一行一行地打印。
    # print(value[0]) # 打印每一行中，第一列的内容。
    # print(value[1]) # 打印每一行中，第二列的内容。以此类推。


"""
excel写入操作
"""
# 找到指定的单元格，对其输入想要写入的内容
# 方法1：如果只是简单的写入，推荐这个方法
# sheet1['A12'] = '这是新写入的内容'
# # 如果有写入操作一定要保存，否则不会生效
# excel.save('./demo.xlsx')
# # 文件操作结束后一定要关闭文件
# excel.close()

# 方法2：
# sheet1.cell(13, 1, "这是复杂的写入方法")
# excel.save('./demo.xlsx')
# excel.close()