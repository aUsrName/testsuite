import time
import pytest

from commands.yaml_util import read_yaml


class Test0202:
    #用法一：最常用的用法
    @pytest.mark.parametrize('caseinfo',read_yaml('./testcases/test_api.yaml'))
    def test_login(self,caseinfo):
        print(f'登录测试用例:{caseinfo}')

    #用法二：不常用，了解即可
    @pytest.mark.parametrize('name,age',[['test1','11'],['test2','22']])
    def test_register(self,name,age):
        print('注册测试用例:%s' % name,age)