from com.huicewang.day3 import DriverFactory
from com.huicewang.day5.NewApi import NewApi

if __name__ == '__main__':
    driver = DriverFactory.create_driver('firefox')
    api = NewApi(driver, r'E:\config.xml')
    api.to(r"http://www.huicewang.com/ecshop/")
    tabs = api.elements('首页', '精品推荐tab')
    total = 0
    for tab in tabs:
        tab.click()
        api.wait(2)
        prices = api.elements('首页', '精品推荐产品价格')
        for price in prices:
            str1 = price.text[1:-1].strip()
            if int(str1) > 10:
                pass
            else:
                print(tab.text + '价格异常' + ':' + str1)
                total += 1
    if total == 0:
        print("价格全部正常")
    api.close()
