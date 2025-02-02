import time

import pytest

#创建fixture固件
@pytest.fixture(scope='function',autouse=True)
def exe_sql():
    print('执行sql语句')
    yield 'success'
    print('用例之后执行：关闭数据库')

class TestApi:

    # def setup_class(self):
    #     print('每个类之前操作，每个类执行一次')
    #
    # def teardown_class(self):
    #     print('每个类之后操作，每个类执行一次')
    #
    # def setup_method(self):
    #     print('每个用例之前操作，每个用例执行一次')
    #
    # def teardown_method(self):
    #     print('每个用例之后操作，每个用例执行一次')

    def test_login(self,exe_sql,base_url):
        print('登录测试用例')
        print(exe_sql,base_url)
        # raise Exception('登录用例失败')

    def test_register(self):
        print('注册测试用例')

