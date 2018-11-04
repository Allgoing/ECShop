import random
import time
import traceback

from selenium.webdriver.support.select import Select

from com.huicewang.day5.XmlParser1 import XmlParser as XP


class NewApi:

    def __init__(self, driver, xml_path):
        self._driver = driver
        self._parse = XP(xml_path)

    def to(self, url):
        try:
            self._driver.get(url)
            time.sleep(2)
            if url == self._driver.current_url:
                return True
            else:
                return False
        except:
            return False

    def wait(self, n):
        time.sleep(n)

    def _get_element(self, page_name, obj_name):
        xpath = './' + page_name + '/' + obj_name
        type = self._parse.get_element_attribute(xpath, 'type')
        value = self._parse.get_element_attribute(xpath, 'value')

        element = None
        if type is not None and value is not None:
            try:
                element = self._driver.find_element(type, value)
            except:
                traceback.print_exc()
        else:
            print(page_name+','+obj_name+'在xml文件中不存在')
        return element

    def elements(self, page_name, obj_name):
        return self._get_elements(page_name, obj_name)

    def _get_elements(self, page_name, obj_name):
        xpath = './' + page_name + '/' + obj_name
        type = self._parse.get_element_attribute(xpath, 'type')
        value = self._parse.get_element_attribute(xpath, 'value')

        elements = None
        if type is not None and value is not None:
            try:
                elements_type = self._driver.find_elements(type, value)
                if elements_type is not None and len(elements_type) > 0:
                    elements = elements_type
            except:
                traceback.print_exc()
        else:
            print(page_name+','+obj_name+'在xml文件中不存在')
        return elements

    def click(self, page_name, obj_name):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            element.click()

    def send_keys(self, page_name, obj_name, text):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            element.click()
            element.clear()
            element.send_keys(text)
            self.wait(1)

    def select_by_value(self, page_name, obj_name, text):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            Select(element).select_by_value(text)
            self.wait(1)

    def select_by_index(self, page_name, obj_name, index):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            select = Select(element)
            if 0 <= index < len(select.options()):
                select.select_by_index(index)
            else:
                select.select_by_index(0)
            self.wait(1)

    def select_the_random(self, page_name, obj_name):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            select = Select(element)
            r = random.randint(0, len(select.options)-1)
            select.select_by_index(r)
            self.wait(1)

    def element_is_exist(self, page_name, obj_name):
        flag = False
        self._driver.implicitly_wait(5)
        element = self._get_element(page_name, obj_name)
        if element is not None:
            flag = True
        return flag

    def element_is_displayed(self, page_name, obj_name):
        if self.element_is_exist(page_name, obj_name):
            try:
                flag = self._get_element(page_name, obj_name).is_display()
                return flag
            except:
                return False

    def element_text(self, page_name, obj_name):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            return element.text

    def element_attribute(self, page_name, obj_name, attribute):
        element = self._get_element(page_name, obj_name)
        if element is not None:
            try:
                return element.get_attribute(attribute)
            except:
                traceback.print_exc('没有'+attribute+'属性')
                return None

    def elements_is_exist(self, page_name, obj_name):
        flag = False
        self._driver.implicitly_wait(5)
        elements = self._get_elements(page_name, obj_name)
        if elements is not None:
            flag = True
        return flag

    def elements_text(self, page_name, obj_name):
        elements = self._get_elements(page_name, obj_name)
        elements_text = []
        if elements is not None:
            for element in elements:
                elements_text.append(element.text)
        return elements_text

    # def elements_attribute(self, page_name, obj_name, attribute):
    #     elements = self._get_elements(page_name, obj_name)
    #     elements_attribute = []
    #     if elements is not None:
    #         for element in elements:
    #             elements_attribute.append(element.get_attribute)
    #     return elements_attribute

    def close(self):
        try:
            self._driver.close()
        except:
            try:
                self._driver.quit()
            except:
                pass