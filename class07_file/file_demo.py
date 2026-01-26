"""
    open函数的应用
        open(文件路径及文件名称, 操作模式, 编码格式)
            1. 文件路径及文件名称：
                文件名称一定要包含文件的后缀名。
                文件路径分为相对路径和绝对路径两种：
                    相对路径：一般会将需要操作的文件保存在工程结构之中，方便直接获取文件。
                            类似于Linux的文件操作系统。通过工程结构，来推导出文件所在的路径位置。
                            例如：
                                ./file_demo.py  表示当前路径下的file_demo.py文件
                                ../class06_exception/exception_demo.py 表示在上一级路径下的class06下的exception文件
                    绝对路径：表示文件在电脑盘符的实际存在的路径位置。
                            例如：D:\Project\Python\hcc_python_class\class07_file\file_demo.py
                            绝对路径只能应用在本地，
                    推荐使用相对路径，尽可能减少绝对路径的使用。

            2. 文件操作模式：用于定义当前我们所获取的文件的具体操作类型。
                r   表示只读模式，允许对文件内容进行读取。但是无法编辑修改。
                w   表示写入模式，允许对文件的写入操作。但是会将文件原有的内容全部情况，以覆盖的形态实现文件的内容写入
                a   表示追加模式，允许对文件的追加写入，默认都是在文件的末尾进行追加
                b   表示二进制模式。一般用于非文本文件内容的操作（图片、视频等）

            3. 编码格式：正确的编码格式可以正常读取文件内容，避免出现乱码。如果要操作的文件可能会有中文，则直接选择utf-8编码格式即可

    文件的操作，一定要与文件的操作模式统一，否则会出问题。
    每一个文件在开启之后，一定记得末尾要调用file.close()释放资源，让文件正常退出，避免不可预见的问题。
    在实际操作文件的过程中，推荐使用try...except...finally来实现对文件操作的管理。因为操作文件过程中如果报错，文件可以正常退出。
    代码在实际编写的过程中，其实你会发现没有你想的那么完整。代码很多功能都是需要自己去设计和实现的。没有那么多现成的东西存在。（例如没有直接的复制函数，复制文件的时候要读->创建要复制的文件->写入）
"""
import traceback

"""
    open函数示例
"""
# file = r'D:\Project\Python\hcc_python_class\class07_file\ROGFlowX16.jpg'  # 绝对路径
# file = r'./ROGFlowX16.jpg'  # 相对路径

# open(file=file, mode='r', encoding='utf-8') # 读取文件内容,基于utf-8编码格式.

# print(open(file=file, mode='r', encoding='utf-8'))    # <_io.TextIOWrapper name='./ROGFlowX16.jpg' mode='r' encoding='utf-8'>

# -----------------------------------------------------------------------

file1 = open(r'./paper1.txt', mode='r', encoding='utf-8')

# 获取文件后的操作行为
"""
    1. 读取文件内容
        file.read()
        file.readline()
        file.readlines()
"""
# print(file.read())  # 获取文件的所有内容。如果文件内容特别多，文件特别大，则读取时可能会出现卡顿现象。


# 读取一行文件内容：在程序运行的过程中，每执行一次，获取一行内容，并将文件的光标移动到新的一行。程序结束后还原
# print(file.readline())  # 一次读取一行
# print("一行读取完毕")
# print(file.readline())  # 一次读取一行


# readlines：获取文件的所有行内容，每一行都是一个单独的元素，并返回一个列表
# print(file.readlines())
# for line in file.readlines():
#     print(line)


"""
    2. 写入文件：单行和多行的写入操作。在程序未终止时，每次写入之后，光标会移至最后方等待下次写入操作。如果程序终止，再写入则是覆盖操作。
        file.write("想写入的内容")
"""
# file2 = open(r'./paper2.txt', mode='w', encoding='utf-8')
# file2.write('这是新写入的文件内容')
#
# file2.write('''
# 多行写入
# 第一行
# 第二行
# 第三行
# ''')


"""
    3. 追加操作（本质也是写入）
"""
# file3 = open(r'./paper3.txt', mode='a', encoding='utf-8')
# file3.write('\n这是追加写入的内容')  # 如果要确保内容写入在文件的最后一行，记得追加内容中要添加\n


# 针对不存在的文件进行写入或者追加，默认会生成对应的文件之后，再继续执行你的写入和追加操作。但是文件夹必须存在
# file = open(r'./paper4.txt', mode='w', encoding='utf-8')   # 可以创建文件，但不可以创建文件夹
# file.write("创建了一个文件\n")
# file.write("第2行")


"""
    4. 二进制模式操作文件
"""
# file4 = open(file='./ROGFlowX16.jpg', mode='rb')    # rb：读取、二进制模式
# print(file4.read())



"""
    操作任意文件，实现文件内容的复制操作
"""
# file5 = open(file='./ROGFlowX16.jpg', mode='rb')    # 原文件内容
# # 生成复制的新文件
# file5_copy = open(file='./ROGFlowX16_copy.jpg', mode='wb')  # wb：写入、二进制模式
#
# content = file5.read()  # 读取文件中的所有内容，保存到content变量中
# file5_copy.write(content)   # 将content写入到新的文件中
#
# file5.close()   # 关闭file5文件
# file5_copy.close()   # 关闭file5_copy文件



"""
    try...except...finally实现对文件操作的管理：对上面的复制文件进行优化
"""
file5 = open(file='./ROGFlowX16.jpg', mode='rb')
file5_copy = open(file='./ROGFlowX16_copy.jpg', mode='wb')
try:
    content = file5.read()
    file5_copy.write(content)
except Exception as e:
    traceback.print_exc()
finally:
    # 文件的关闭是逐个进行的，所以你开启有多少文件就记得关闭多少文件。一般是用完就要直接close。
    file5.close()
    file5_copy.close()













