from selenium import  webdriver
import time
import api_618 as api
if __name__ == '__main__':

    driver = api.setup('ff', 'http://www.huicewang.com/ecshop')
    tabs = driver.find_elements_by_xpath("//div[@id='itemBest']/h2/a")
    for tab in tabs:
        flag = 0
        tab.click()
        time.sleep(1)
        prices = driver.find_elements_by_xpath("//div[@id='show_best_area']//font[@class='f1']")
        for price in prices:
            p = price.text[1:-1].strip()
            if p == '' or p == '0' or p == None:
                print(tab.text+u' 价格异常:' + p)
                flag += 1
        if flag == 0:
            print(tab.text+u' 价格无异常')