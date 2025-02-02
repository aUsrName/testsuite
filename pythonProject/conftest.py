import pytest


#创建fixture固件
@pytest.fixture(scope = 'function', autouse=True)
def exe_order():
    print('用例之前，订单之前')
    yield
    print('用例之后：订单之后')