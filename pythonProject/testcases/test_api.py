import time

import allure


@allure.epic('项目名称：通用接口框架参考')
@allure.feature('模块名称：用户管理')
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
    @allure.story('接口名称：登录接口')
    @allure.title('用例名称：验证登录接口成功返回数据')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description('用户的登录接口成功用例')
    @allure.link('接口地址')
    @allure.issue('bug地址')
    @allure.testcase('用例地址')
    def test_login1(self):
        allure.step('第一步')
        print('登录测试成功用例')
        allure.step('第二步')
        # raise Exception('登录用例失败')

    @allure.story('接口名称：登录接口')
    @allure.title('用例名称：验证登录接口失败')
    def test_login2(self):
        #加入测试用例步骤,加测试附件（错误截图）
        for i in range(1, 6):
            with allure.step(f'第{i}步'):
                print(f'步骤{i}')
        with allure.step('第7步：步骤7'):
            with open('D:\\aaa.jpg',mode='rb') as f:
                allure.attach(body=f.read(),name='第7步图片',attachment_type=allure.attachment_type.JPG)
        #接口自动化加请求方式、路径等
        allure.attach(body='get',name='请求方法',attachment_type=allure.attachment_type.TEXT)
        print('登录测试失败用例')
        # raise Exception('登录用例失败')

    @allure.story('接口名称：注册接口')
    def test_register(self,exe_order):
        allure.dynamic.title('用例名称：注册测试用例')
        allure.dynamic.description('注册接口测试用例')
        allure.dynamic.link('接口地址')
        allure.dynamic.issue('bug地址')
        allure.dynamic.testcase('用例地址')
        print('注册测试用例')


