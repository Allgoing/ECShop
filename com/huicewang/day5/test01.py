import unittest

from com.huicewang.day3 import DriverFactory
from com.huicewang.day5.NewApi import NewApi


class Test(unittest.TestCase):

    api = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.create_driver('firefox')
        cls.api = NewApi(cls.driver, r'E:\config.xml')
        cls.api.to('http://www.huicewang.com/ecshop/index.php')

    @classmethod
    def tearDownClass(cls):
        cls.api.close()

    # def setUp(self):
    #     driver = DriverFactory.create_driver('firefox')
    #     self.api = NewApi(driver, r'E:\config.xml')
    #     self.api.to('http://www.huicewang.com/ecshop/index.php')
    #
    # def tearDown(self):
    #     self.api.close()

    def test_case01(self):
        api = self.api
        api.click('首页', '登录按钮')
        api.wait(2)
        api.send_keys('登录页', '用户名', 'zach')
        api.send_keys('登录页', '密码', '123456')
        api.click('登录页', '登录按钮')
        api.wait(5)

        try:
            if api.elements_text('首页', '登录标示') == 'zach':
                print('登陆成功')
            else:
                print('登陆失败1')
        except:
            print('登陆失败2')

    def test_case02(self):
        # 用对象定位引擎编写测试用例
        api = self.api
        api.select_by_value('首页', '分类', '3')
        api.send_keys('首页', '关键词', '诺基亚')
        api.click('首页', '搜索按钮')
        flag = 0
        if api.elements_is_exist('搜索结果页', "商品"):
            prices = api.elements_text('搜索结果页', "商品价格")
            for p in prices:
                p = p[1:-1].strip()
                if p == '' or p == '0' or p is None:
                    flag += 1
                    print('价格异常:') + p
            if flag == 0:
                print('价格全部正确')
        else:
            print('未搜索出产品')

if __name__ == '__main__':
    unittest.main()