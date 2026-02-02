"""
    比较推荐的一种单文件的操作语法结构————with open
    with open语法应用：
        通过with open的语法结构，在文件操作结束后，会自动调用close方法，无需手动调用。
        语法：
            with open(filename, mode, encoding) as 别名:
                文件操作代码块
        1. open的调用与常规方法一致。
        2. 对文件进行操作的时候，同意通过别名来替代文件。
        3. 一般用于操作单个文件。
"""

"""
    with open 示例
"""
# with open(file='./paper1.txt', mode='r', encoding='utf-8') as file1:
#     # print(file1.read())
#     content = file1.read()
#
# print(content)  # 在with open语法块外部依旧可以调用with open所产生的数据

print("--------------------------------")

"""
    重要：⚠ 文件的读取机制：
        程序在执行的时候，有它们自己的文件路径。
        在哪里执行代码，初始路径就在哪里。
            假如在main.py中要调用read_file()方法，则应该写：print(read_file('./class07_file/paper1.txt'))。初始路径为main.py开始
        如果程序在执行的时候使用的是相对路径，则需要考虑程序的初始路径；如果应用的是绝对路径，则不需要考虑该问题。
        
            推荐在封装读取文件函数时，【优先将文件路径作为参数进行传入】。方便路径问题的解决。
"""
# 一般在操作文件的时候，都会封装一个文件的操作函数
# 封装文件的操作函数
def read_file(file):    # 调用时传入文件路径
    with open(file=file, mode='r', encoding='utf-8') as file2:
        content = file2.read()
    return content

# 绝对路径函数
# def read_file():
#     with open(file='D:\Project\Python\hcc_python_class\class07_file\paper1.txt', mode='r', encoding='utf-8') as file3:
#         content = file3.read()
#     return content

# 调用文件操作函数。在其他文件调用read_file()在main.py中
# print(read_file(r'./paper1.txt'))