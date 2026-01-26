"""
    logging库的基本使用
        日志库的使用没有所谓的逻辑的概念，一切的内容都是基于配置和展示为主。所以在实际使用的时候，就是对其进行各类的配置和调用。
            1. 创建日志对象，进行对应的设置
            2. 调用日志对象
            3. 基于不同的日志等级，来区分不同的内容。
                日志的五种等级：debug < info < warning(default，默认级别) < error < critical
        日志的内容不是自动生成的，所有的日志内容都是人为定义的内容。
        在哪里出现日志，出现什么内容的日志，以什么格式来显示的日志，都是我们提前定义好的。所以可以理解为是进阶的print
        日志等级的定义也是基于你自己的决定来定义的。需要输出什么等级的日志完全由你自己决定。

        日志显示：如果定义了filename参数，则不会在控制台中显示，而是全部写入文件之中。

        日志库的配置：
            1. 创建日志对象
            2. 设置日志的等级
            3. 设置日志的输出格式
            4. 设置日志的输出渠道
"""
import logging

"""
    logging的示例
"""
logging.basicConfig(
    level=logging.DEBUG,  # 设置日志的等级，默认为warning，但可以自行修改

    # 日志的格式设置：整体的设置就是基于str内容来定义。
    # levelname表示日志等级，asctime表示时间，filename表示执行文件，lineno表示执行行数，message表示执行文本信息
    format='%(levelname)s %(asctime)s %(filename)s %(lineno)s : %(message)s',
    encoding = 'utf-8',
    filename='./log/log.log' # 设置日志的保存路径
)

# 调用日志对象，实现日志的输出：
logging.debug("这是debug级别的日志")
logging.info("这是info级别的日志")
logging.warning("这是warning级别的日志")
logging.error("这是error级别的日志")
logging.critical("这是critical级别的日志")


