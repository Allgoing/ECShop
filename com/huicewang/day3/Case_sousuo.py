import DriverFactory
from com.huicewang.day3.HC import HC
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    hc = HC(DriverFactory.create_driver('firefox'))
    hc.to(r'http://www.huicewang.com/ecshop/')
    hc.selectByValue(By.ID, 'category', '3')
    hc.send_keys(By.ID, 'keyword', '诺基亚')
    hc.click(By.NAME, 'imageField')
    if hc.isElementsExist(By.XPATH, "//div[@class='clearfix goodsBox']/div"):
        prices = hc.elementsText(By.XPATH, r"//div[@class='clearfix goodsBox']/div//font")
        for price in prices:
            str1 = price[1:-1]
            if int(str1) > 1:
                pass
            else:
                print("价格不正常")
        else:
            print("价格正常")
    else:
        print('顶部搜索功能不正常1')

    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.get(r"http://www.huicewang.com/ecshop/")
    # driver.implicitly_wait(10)
    #
    # element = driver.find_element_by_id('category')
    # select = Select(element)
    # select.select_by_value('3')
    # input = driver.find_element_by_id('keyword')
    # input.click()
    # input.clear()
    # input.send_keys('诺基亚')
    # driver.find_element_by_name('imageField').click()
    # # noinspection PyBroadException
    # try:
    #     elements = driver.find_elements_by_xpath("//div[@class='clearfix goodsBox']/div")
    #     if len(elements) > 0:
    #         print('顶部正常，搜索到%d个商品' % len(elements))
    #         prices = driver.find_elements_by_xpath(r"//div[@class='clearfix goodsBox']/div//font")
    #
    #         str1 = ''
    #         for price in prices:
    #             str1 = price.text[1:-1]
    #             if int(str1) > 1:
    #                 pass
    #             else:
    #                 print("价格不正常")
    #         else:
    #             print("价格正常")
    #
    #     else:
    #         print('顶部搜索功能不正常1')
    # except:
    #     print('顶部搜索功能不正常2')