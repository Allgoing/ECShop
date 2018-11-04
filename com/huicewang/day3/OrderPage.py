import time
from selenium import webdriver

class OrderPage

    url = r'http://www.huicewang.com/ecshop/user.php?act=order_list'

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(OrderPage.url)
        time.sleep(2)

    def search_order(self, order_id):
        driver = webdriver.Firefox()
        info = []
        trs = driver.find_elements_by_xpath(r'//div[@class='userCenterBox boxCenterList clearfix']/table//tr')
        for i in range(1, len(trs)):
            if trs[i].find_elements_by_tag_name('td')[0] == order_id:
                for td in trs[i].find_elements_by_tag_name('td'):
                    info.append(td.text)
        return info