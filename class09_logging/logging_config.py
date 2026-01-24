"""
    基于日志的配置形态，实现内容的获取。用于创建记录器进行日志内容的生成。
    如果内容有误。一般报错的信息会提示KeyError
"""
import logging.config
import pathlib

# 读取配置文件的日志项
def get_logger():
    # 配置文件的路径
    # file = './log_conf.ini'   # 不合适-->下一行进行更新
    file = pathlib.Path(__file__).parents[0] / 'log_conf.ini'   # pathlib.Path(__file__)：获取当前执行文件的绝对路径；parents[0]：获取上级路径；/：路径拼接符；'log_conf.ini'：文件名。

    # 基于ini文件实现日志的配置项
    logging.config.fileConfig(file, encoding='utf-8')
    # 创建日志记录器
    logger = logging.getLogger()
    # 一定要返回日志记录器，否则无法使用。
    return logger

log = get_logger()
log.info('这个是配置文件的info')


"""
    基于pathlib库来实现对文件路径的处理：
        通过获取当前执行文件的绝对路径，然后反向推导出需要的文件的绝对路径。
"""
# file_path = pathlib.Path(__file__)  # 以当前路径为起点，获取当前文件的绝对路径，返回对象是路劲对象。
# print(file_path)    # D:\Project\Python\hcc_python_class\class09_logging\logging_config.py
# print(type(file_path))  # 路径对象： <class 'pathlib.WindowsPath'>

"""
    反向推导：
    因为是路径对象，所以不需要字符串的拼接，直接通过 / 来实现路径的拼接即可。
    因为已有当前文件的绝对路径，所以推导时需要关联到文件的上下级
    parents查找父类，通过下标来查找父类，0是上级，1是上上级，2是上上上级。。。。。
"""
# file = pathlib.Path(__file__).parents[0].resolve() / 'log_conf.ini' # resolve是执行的意思，执行当前内容并生成结果，之后进行拼接
# print(file)