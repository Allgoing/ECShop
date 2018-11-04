from selenium import  webdriver
import time
from selenium.webdriver.support.select import Select
from HC import HC
import DriverFactory
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    driver = DriverFactory.creat_driver('ff')
    hc = HC(driver)
    hc.to('http://www.huicewang.com/ecshop/index.php')
    hc.selectByValue(By.ID, 'category', '3')
    hc.wait(1)
    hc.sendKeys(By.ID,'keyword',u'诺基亚')
    hc.click(By.NAME,'imageField')
    hc.wait(2)
    flag = 0
    if hc.isElementsExist(By.XPATH,"//div[@class='clearfix goodsBox']/div[@class='goodsItem']"):
        prices = hc.elementsText("//form[@id='compareForm']//font[@class='shop_s']")
        for p in prices:
            p = p[1:-1].strip()
            if p == '' or p == '0' or p == None:
                flag += 1
                print('价格异常:' + p)

        if flag==0:
            print('价格全部正确')
    else:
        print('未搜索出产品')