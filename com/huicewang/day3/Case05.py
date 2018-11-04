import traceback
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    orderNumber = '0'
    try:
        driver.maximize_window()
        driver.get(r'http://www.huicewang.com/ecshop/')
        driver.implicitly_wait(10)

        # 使用cookie登录
        driver.add_cookie({'name': 'ECS[password]', 'value': 'b3778dc5d587f8f152b76304724aa313'})
        driver.add_cookie({'name': 'ECS[user_id]', 'value': '11'})
        driver.add_cookie({'name': 'ECS[username]', 'value': 'zach'})

        driver.find_element_by_xpath(r"//div[@id='show_best_area']//a").click()
        driver.find_element_by_xpath(r"//form[@id='ECS_FORMBUY']//li[@class='padd']/a[1]").click()
        driver.find_element_by_xpath(r"//img[@alt='checkout']//..").click()
        driver.find_element_by_xpath(r"//input[@src='themes/default/images/bnt_subOrder.gif']").click()
        orderNumber = driver.find_element_by_xpath(r"//div[@class='flowBox']//font").text
        print(orderNumber)
        if orderNumber != '0':

            driver.get(r"http://www.huicewang.com/ecshop/user.php?act=order_list")
            orders = driver.find_elements_by_xpath(r"//a[@class='f6']")
            if len(orders) > 0:
                for order in orders:
                    if orderNumber == order.text:
                        print("下单成功")
            else:
                print("下单失败")
        else:
            print('下单失败')
    except:
        traceback.print_exc()
        print("下单失败")