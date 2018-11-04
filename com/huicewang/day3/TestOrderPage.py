from com.huicewang.day3 import DriverFactory
from com.huicewang.day3 import LoginPage
from com.huicewang.day3 import OrderPage

if __name__ == '__main__':

    driver = DriverFactory.create_driver('firefox')
    LoginPage(driver).login('chaper', '123456')
    OrderPage(driver).search_order('2018012432769')