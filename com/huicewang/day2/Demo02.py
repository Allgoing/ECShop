from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import random

if __name__ == '__main__':
    # driver = webdriver.Firefox()
    # driver.get('file:///E:/demo.html')
    # driver.maximize_window()
    # time.sleep(2)
    #
    # element = driver.find_element_by_name('checkbox2')
    # # if not element.is_selected():
    # #     element.click()
    # elements = driver.find_elements_by_xpath("//div[@id='checkbox']/input[@type='checkbox']")
    # for element in elements:
    #     if not element.is_selected():
    #         element.click()
    a = 1
    b = 1
    print(a, end=" ")
    n = 20
    while n > 1:
        a, b = b, a+b
        print(a, end=" ")
        n -= 1



