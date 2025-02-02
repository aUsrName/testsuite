import pytest

#创建fixture固件
@pytest.fixture(scope = 'function', autouse=True)
def exe_sql():
    print('用例之前，执行sql语句')
    yield
    print('用例之后执行：关闭数据库')
