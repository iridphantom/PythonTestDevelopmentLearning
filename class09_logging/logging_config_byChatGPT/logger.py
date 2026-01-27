import logging
import logging.config
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_logger(name="autotest"):
    # 1. 创建 log 目录
    log_dir = os.path.join(BASE_DIR, "log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 2. 按日期生成日志文件名
    log_file = time.strftime("%Y-%m-%d.log")

    log_path = os.path.join(log_dir, log_file)

    # 3. 加载 logging 配置文件（注入 logfile 变量）
    config_path = os.path.join(BASE_DIR, "logging.ini")
    logging.config.fileConfig(
        config_path,
        defaults={"logfile": log_path},
        disable_existing_loggers=False
    )

    return logging.getLogger(name)