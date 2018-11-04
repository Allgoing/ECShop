import time
from selenium import webdriver
import re
if __name__ == '__main__':
    driver = webdriver.Firefox()
    # driver.get('http://www.baidu.com/')
    # time.sleep(2)
    driver.get('http://www.huicewang.com/ecshop/')
    # time.sleep(2)
    # driver.forward()
    # time.sleep(2)
    # driver.back()
    # time.sleep(2)
    # driver.refresh()
    # print(driver.title)
    # print(driver.current_url)
    # 正则表达式
    # source = driver.page_source
    # all_links = re.findall(r'<a.*?/a>', source)
    # for links in all_links:
    #     print(links)
    # print(len(all_links))
    # 窗口最大化和设置大小
    # driver.maximize_window()
    # driver.set_window_size(400, 800)
    # 截图
    driver.get_screenshot_as_file('e:/1.png')
