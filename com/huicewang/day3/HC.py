import traceback
import time
import random
from selenium.webdriver.support.select import Select


class HC:

    def __init__(self, driver):
        self._driver = driver

    def to(self, url):
        try:
            self._driver.get(url)
            return True
        except:
            return False

    def send_keys(self, by, value, text):
        try:
            element = self._driver.find_element(by, value)
            element.click()
            element.clear()
            element.send_keys(text)
            self._driver.implicitly_wait(10)
        except:
            traceback.print_exc()

    def click(self, by, value):
        try:
            self._driver.find_element(by, value).click()
        except:
            traceback.print_exc()

    def wait(self, s):
        time.sleep(s)

    def select_by_value(self, by, value, text):
        try:
            element = self._driver.find_element(by, value)
            Select(element).select_by_value(text)
            self.wait(1)
        except:
            traceback.print_exc()

    def select_by_index(self, by, value, index):
        try:
            element = self._driver.find_element(by, value)
            Select(element).select_by_index(index)
            self.wait(1)
        except:
            traceback.print_exc()

    def select_random(self, by, value):
        try:
            element = self._driver.find_element(by, value)
            select = Select(element)
            select.select_by_index(random.randint(0, len(select.options)-1))
            self.wait(1)
        except:
            traceback.print_exc()

    def is_element_exist(self, by, value):
        flag = False
        try:
            self._driver.implicitly_wait(5)
            self._driver.find_element(by, value)
            flag = True
        except:
            traceback.print_exc()
        return flag

    def is_element_display(self, by, value):
        if self.is_element_exist(by, value):
            try:
                return self._driver.find_element(by, value).is_displayed()
            except:
                return False
        else:
            return False

    def is_element_enable(self, by, value):
        if self.is_element_display(by, value):
            try:
                return self._driver.find_element(by, value).is_enable()
            except:
                return False
        else:
            return False

    def get_value(self, by, value, attri):
        value_text = None
        if self.is_element_display(by, value):
            try:
                if attri == 'text':
                    value_text = self._driver.find_element(by, value).text
                else:
                    value_text = self._driver.find_element(by, value).get_attribute(attri)
            except:
                traceback.print_exc()

        return value_text

    def is_elements_exist(self, by, value):
        try:
            elements = self._driver.find_elements(by, value)
            if len(elements) > 0:
                return True
            else:
                return False
        except:
            traceback.print_exc()

    def elements_text(self, by, value):
        texts = []
        if self.is_elements_exist(by, value):
            elements = self._driver.find_elements(by, value)
            for element in elements:
                texts.append(element.text)
            return texts
        return texts