from com.huicewang.day3 import DriverFactory
from com.huicewang.day5.NewApi import NewApi

if __name__ == '__main__':
    # 用对象定位引擎编写测试用例
    driver = DriverFactory.create_driver('firefox')
    api = NewApi(driver, 'config.xml')
    api.to('http://www.huicewang.com/ecshop')
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
                print('价格异常:')+p
        if flag == 0:
            print('价格全部正确')
    else:
        print('未搜索出产品')
    api.close()