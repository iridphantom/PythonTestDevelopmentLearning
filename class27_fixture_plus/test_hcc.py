import logging

import pytest

# 创建一个logger，便于生成需要的log信息
logger = logging.getLogger(__name__)


@pytest.mark.login
def test_hcc(hcc, session_hcc):
    print('hcc test case')
    print(session_hcc)
    logger.debug('这是debug信息')
    logger.info('这是info信息')
    logger.error('这是error信息')
    logger.warning('这是warning信息')

if __name__ == '__main__':
    pytest.main(['./test_hcc.py'])