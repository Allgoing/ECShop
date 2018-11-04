from selenium import webdriver
import time


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(r"http://www.huicewang.com/ecshop/")
    driver.implicitly_wait(10)

    elements = driver.find_elements_by_xpath(r"//div[@id='itemBest']//h2")
    total = 0
    for element in elements:
        element.click()
        time.sleep(2)
        prices = driver.find_elements_by_xpath(r"//div[@id='show_best_area']//font")
        for price in prices:
            str1 = price.text[1:-1].strip()
            if int(str1) > 100:
                pass
            else:
                print(element.text + '价格异常' + ':' + str1)
                total += 1
    print(total)
    if total == 0:
        print("价格全部正常")