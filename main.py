import pathlib
import time

from class07_file.file_demo2 import read_file
from class09_logging.logging_config import get_logger
from class09_logging.homework_logging_config.logger import LoggerSetup

if __name__ == '__main__':

    print(read_file('./class07_file/paper1.txt'))
    # print(read_file('./README.md'))

    # log = get_logger()
    # log.info('这个是配置文件的info')






"""
测试调用封装的logging配置文件：
测试调用封装的logging配置文件：
测试调用封装的logging配置文件：
测试调用封装的logging配置文件：


def simulate_daily_activity(day_name):
    # 模拟一天的活动
    logger = LoggerSetup.get_logger(__name__)

    logger.info(f"开始处理 {day_name} 的任务")
    logger.debug(f"{day_name} - 调试信息")
    logger.warning(f"{day_name} - 警告信息")
    logger.error(f"{day_name} - 错误信息")

    # 模拟一些业务逻辑
    try:
        result = 10 / 2
        logger.info(f"{day_name} - 计算结果: {result}")
    except Exception as e:
        logger.error(f"{day_name} - 计算出错: {e}")

    logger.info(f"{day_name} 的任务处理完毕\n")


def main():
    # 设置日志配置
    LoggerSetup.setup_logging()

    logger = LoggerSetup.get_logger(__name__)
    logger.info("=== 应用程序启动 ===")

    # 模拟连续几天的活动（实际运行时，每天的日志会自动滚动）
    days = ["周一", "周二", "周三"]
    for day in days:
        simulate_daily_activity(day)
        time.sleep(1)  # 模拟时间间隔

    logger.info("=== 应用程序正常关闭 ===")


if __name__ == "__main__":
    main()

"""