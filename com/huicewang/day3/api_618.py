import time
from selenium import webdriver


# 创建一个driver，刷新到其实连接，窗口最大化，等待两秒
def setup(browser, url):
    browser = browser.strip().lower()
    if browser == 'firefox':
        try:
            driver = webdriver.Firefox()
        except:
            return None
    elif browser == 'chrome':
        try:
            driver = webdriver.Chrome()
        except:
            return None
    elif browser == 'ie':
        try:
            driver = webdriver.Ie()
        except:
            return None
    else:
        print("不存在的浏览器类型：火狐，谷歌，Ie")
        return None

    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(10)
    return driver


def login(driver, username, pwd):

    driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[1]").click()
    time.sleep(2)
    user = driver.find_element_by_name('username')
    user.click()
    user.clear()
    user.send_keys(username)

    password = driver.find_element_by_name('password')
    password.click()
    password.clear()
    password.send_keys(pwd)

    driver.find_element_by_name('submit').click()
    time.sleep(5)
    try:
        u_name = driver.find_element_by_class_name('f4_b').text
        if u_name == username:
            return True
        else:
            return False
    except:
        return False
