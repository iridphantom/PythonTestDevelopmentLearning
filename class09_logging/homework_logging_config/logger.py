import logging
import logging.config
import os
import pathlib
import sys
from logging.config import fileConfig


class LoggerSetup:
    logging_config_file = pathlib.Path(__file__).resolve().parent / 'logging.ini'

    @staticmethod
    def setup_logging(config_path=logging_config_file, default_level=logging.INFO):
        """
        设置日志配置，优先使用配置文件，否则使用默认配置
        修复路径问题：使用原始字符串和正斜杠
        """
        # 获取 logging.ini 所在目录
        config_dir = os.path.dirname(config_path)
        log_dir = os.path.join(config_dir, 'logs')

        # 确保日志目录存在
        os.makedirs(log_dir, exist_ok=True)
        logging.info(f"确保日志目录 {log_dir} 存在")

        # 读取配置文件内容
        with open(config_path, 'r') as f:
            config_lines = f.readlines()

        # 修复路径：使用原始字符串和正斜杠
        new_config_lines = []
        for line in config_lines:
            # 仅替换文件路径部分（使用原始字符串避免转义问题）
            if "args = ('logs/app.log'" in line:
                # 创建绝对路径（使用正斜杠，避免Windows转义问题）
                absolute_log_path = os.path.normpath(os.path.join(log_dir, 'app.log'))
                # 替换为原始字符串（避免额外转义）
                absolute_log_path = absolute_log_path.replace('\\', '/')
                # 替换配置文件中的路径
                new_line = line.replace("logs/app.log", absolute_log_path)
                new_config_lines.append(new_line)
            else:
                new_config_lines.append(line)

        # 保存临时配置文件
        temp_config = os.path.join(config_dir, 'temp_logging.ini')
        with open(temp_config, 'w') as f:
            f.writelines(new_config_lines)

        # 使用临时配置文件加载
        if os.path.exists(temp_config):
            logging.config.fileConfig(temp_config)
            logging.info(f"日志配置已从 {temp_config} 加载")
            # 删除临时文件
            os.remove(temp_config)
        else:
            logging.basicConfig(level=default_level)
            logging.warning(f"日志配置文件 {temp_config} 不存在，使用默认配置")

    @staticmethod
    def get_logger(name=__name__, level=None):
        logger = logging.getLogger(name)
        if level is not None:
            logger.setLevel(level)
        return logger