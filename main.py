import pathlib

from class09_logging.logging_config import get_logger

if __name__ == '__main__':
    log = get_logger()
    log.info('这个是配置文件的info')