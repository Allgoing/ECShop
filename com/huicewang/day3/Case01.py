import time
import api_618 as api

from com.huicewang.day3 import DriverFactory

if __name__ == '__main__':

    # driver = api.setup('ff','http://www.huicewang.com/ecshop')
    driver = DriverFactory.create_driver('firefox')
    driver.get('http://www.huicewang.com/ecshop')

    driver.find_element_by_xpath("//font[@id='ECS_MEMBERZONE']/a[1]").click()
    time.sleep(2)
    user = driver.find_elements(name, 'username')
    # user = driver.find_element_by_name('username')
    user.click()
    user.clear()
    user.send_keys('zach')

    password = driver.find_element_by_name('password')
    password.click()
    password.clear()
    password.send_keys('123456')

    driver.find_element_by_name('submit').click()
    time.sleep(5)
    try:
        u_name = driver.find_element_by_class_name('f4_b').text
        if u_name == 'zach':
            print('登录成功')
        else:
            print('登录失败')
    except:
        print('登录失败')