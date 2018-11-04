from selenium.webdriver.common.by import By
import time


class LoginPage:

    url = r'http://www.huicewang.com/ecshop/user.php'
    username_type = By.NAME
    username_value = 'username'

    pwd_type = By.NAME
    pwd_value = 'password'

    submit_type = By.NAME
    submit_value = 'submit'

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(LoginPage.url)
        time.sleep(2)

    def login(self, user_name, pwd_text):
        username = self._driver.find_element(LoginPage.username_type, LoginPage.username_value)
        username.click()
        username.clear()
        username.sendKeys(user_name)

        pwd = self._driver.find_element(LoginPage.pwd_type, LoginPage.pwd_value)
        pwd.click()
        pwd.clear()
        pwd.sendKeys(pwd_text)

        self._driver.find_element(LoginPage.submit_type, LoginPage.submit_value).click()
        time.sleep(5)
