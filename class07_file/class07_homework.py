"""
    熟悉文件操作相关内容
    封装自己的文件操作函数
    搞清楚文件的读取路径机制问题。

    那假设我要搜索文件中的某段内容，然后修改指定的内容，该怎么做？
"""
import pathlib

from pathlib import Path

# 创建一个路径
p = Path('./paper4.txt')
print(p)    #  paper4.txt
print(type(p))    # <class 'pathlib.WindowsPath'>


"""
    如果需要根据程序运行时的上下文操作文件，使用 Path.cwd()。
    如果需要定位与脚本相关的资源文件（如配置文件、数据文件等），使用 Path(__file__).parent 更可靠。
"""

# 获取当前工作目录（Current Working Directory）
print(Path.cwd())  # D:\Project\Python\hcc_python_class\class07_file


# 获取当前脚本文件所在的目录（不包括文件名）
# __file__ 是 Python 内置变量，表示当前脚本的绝对路径，.parent 则提取其父目录
print(Path(__file__).parent)    # D:\Project\Python\hcc_python_class\class07_file

# 路径属性与信息获取
print(p.name)       # 文件名：paper4.txt
print(p.stem)       # 主名：paper4
print(p.suffix)     # 后缀：.txt
print(p.parent)     # 上级目录：.
print(p.parts)      # 路径分段：('paper4.txt',)
print(p.is_absolute())  # 是否绝对路径 False

# 判断是否是文件或目录
print(p.is_file())
print(p.is_dir())


# 判断文件或目录是否存在
p.exists()      # True / False


# 创建目录
# parents=True：自动创建上层目录
# exist_ok=True：存在时不报错
Path("./data").mkdir(parents=True, exist_ok=True) # 在当前目录下创建data文件夹

# 删除空目录。
# 如果目录不是空的，则会报错：OSError: [WinError 145] 目录不是空的。: 'data'
Path("./data").rmdir()


# 删除文件
Path("./asd/asd.txt").unlink(missing_ok=True)