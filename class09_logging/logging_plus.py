"""
    logging库的四大组件：
        1. logger记录器：提供基本能够被程序直接调用的接口（方法）
        2. handler处理器：提供将记录器的内容展示到具体的目的地的用途。也就是控制台 / 文件。
        3. filter过滤器：提供更加细化的内容控制
        4. formatter格式化器：提供日志的所有输出格式

"""
import logging

# 创建logger记录器，实现对日志的记录行为：
logger = logging.getLogger('root')  # 创建日志记录器，并指定日志记录器的名称为root

# formatter定义日志格式
logging_formatter = logging.Formatter('%(levelname)s %(asctime)s %(filename)s %(lineno)s : %(message)s')

# logger日志等级的设置
logger.setLevel(logging.WARNING)  # 只记录warning及以上的日志


# handler处理器创建：控制台处理器（在控制台中输出）
stream_handler = logging.StreamHandler()    # 创建控制台处理器
# 设置处理器的日志等级
stream_handler.setLevel(logging.INFO)   # 控制台处理器只记录info及以上的日志
# 设置处理器显示格式
stream_handler.setFormatter(logging_formatter)


# 创建处理器：文件处理器，用于将日志记录保存到文件之中
file_handler = logging.FileHandler(filename='./log/log_plus.log', encoding='utf-8')
# 设置文件处理器的日志等级
file_handler.setLevel(logging.DEBUG)
# 设置文件处理器的显示格式
file_handler.setFormatter(logging_formatter)

# 将stream_handler添加到logger之中
logger.addHandler(stream_handler)
# 将file_handler添加到logger之中
logger.addHandler(file_handler)

# 日志输出
logging.debug("这是debug级别的日志")
logging.info("这是info级别的日志")
logging.warning("这是warning级别的日志")
logging.error("这是error级别的日志")
logging.critical("这是critical级别的日志")