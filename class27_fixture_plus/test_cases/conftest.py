import pytest

@pytest.fixture
def hcc(request):
    def hcc_finalizer():
        print('hcc child的后置执行')

    request.addfinalizer(hcc_finalizer)

    print('hcc child的前置执行')