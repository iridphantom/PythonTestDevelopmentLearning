"""
    1. 熟悉pathlib的文件路径获取方式
    2. 配置自己的日志配置文件，不需要背，多熟悉即可。封装自己的日志记录器获取函数。
"""
import pathlib

# 获取D:\Project\Python\hcc_python_class\main.py
file_path1 = pathlib.Path(__file__).parents[1] / 'main.py'

print(file_path1)



# 加上.resolve()
file_path2 = pathlib.Path(__file__).parents[1].resolve() / 'main.py'

print(file_path2)