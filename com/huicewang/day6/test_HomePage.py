from com.huicewang.day6.TestBase import TestBase


class HomePage(TestBase):

    def test_case01(self):
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

    def test_case02(self):
        api = self.api
        check = self.check
        tabs = api.elements('首页', '精品推荐tab')
        for tab in tabs:
            tab.click()
            api.wait(2)
            prices = api.elements('首页', '精品推荐产品价格')
            for price in prices:
                p = price.text[1:-1].strip()
                check.notIn(p, ['', '0', None], '价格异常' + p)
                check.greater(int(p), 100, '价格异常' + p)
        check.result('价格全部正常')