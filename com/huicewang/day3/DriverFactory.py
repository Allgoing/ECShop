from selenium import webdriver

def create_driver(str_browser):
    browser = str_browser.strip().lower()
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
        print("无效的浏览器类型：")+str_browser

    if driver is not None:
        driver.maximize_window()
        driver.implicitly_wait(10)

    return driver