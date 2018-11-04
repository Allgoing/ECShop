import ddt

from com.huicewang.day6.TestBase import TestBase
from com.huicewang.day6.CSV import CSV


@ddt.ddt
class LoginPage(TestBase):

    csv = CSV('E:\login.csv')
    info = csv.get_all()

    @ddt.data(*info)
    def test_case01(self, info):
        api = self.api
        api.click('首页', '登录按钮')
        api.wait(2)
        api.send_keys('登录页', '用户名', info['username'])
        api.send_keys('登录页', '密码', info['pwd'])
        api.click('登录页', '登录按钮')
        api.wait(5)

        try:
            if api.element_text('首页', '登录标示') == info['username']:
                print('登陆成功')
            else:
                print('登陆失败1')
        except:
            print('登陆失败2')