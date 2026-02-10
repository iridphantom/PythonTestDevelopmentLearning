import pytest

# from class27_fixture_plus.conftest import hcc

def test_func(hcc, session_hcc):
    print('子路径下的Fixture调用')
    print(session_hcc)


if __name__ == '__main__':
    pytest.main(['-sv', './test_child.py'])
