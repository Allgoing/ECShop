from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(r"http://www.huicewang.com/ecshop/")
    driver.implicitly_wait(10)

    element = driver.find_element_by_id('category')
    select = Select(element)
    select.select_by_value('3')
    input = driver.find_element_by_id('keyword')
    input.click()
    input.clear()
    input.send_keys('诺基亚')
    driver.find_element_by_name('imageField').click()
    # noinspection PyBroadException
    try:
        elements = driver.find_elements_by_xpath("//div[@class='clearfix goodsBox']/div")
        if len(elements) > 0:
            print('顶部正常，搜索到%d个商品' % len(elements))
            prices = driver.find_elements_by_xpath(r"//div[@class='clearfix goodsBox']/div//font")

            str1 = ''
            for price in prices:
                str1 = price.text[1:-1]
                if int(str1) > 1:
                    pass
                else:
                    print("价格不正常")
            else:
                print("价格正常")

        else:
            print('顶部搜索功能不正常1')
    except:
        print('顶部搜索功能不正常2')