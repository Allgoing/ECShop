import traceback
from selenium import webdriver
from com.huicewang.day3 import api_618
# from com.huicewang.day3 import LoginPage

if __name__ == '__main__':

    orderNumber = '0'
    try:
        driver = api_618.setup('Firefox ', r'http://www.huicewang.com/ecshop/')
        # 使用cookie登录
        # driver.add_cookie({'name': 'ECS[password]', 'value': 'b3778dc5d587f8f152b76304724aa313'})
        # driver.add_cookie({'name': 'ECS[user_id]', 'value': '11'})
        # driver.add_cookie({'name': 'ECS[username]', 'value': 'zach'})
        # 使用api调用
        if api_618.login(driver, 'chaper', '123456'):

            driver.find_element_by_xpath(r"//div[@id='show_best_area']//a").click()
            driver.find_element_by_xpath(r"//form[@id='ECS_FORMBUY']//li[@class='padd']/a[1]").click()
            driver.find_element_by_xpath(r"//a[@href='flow.php?step=checkout']").click()
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
        else:
            print("登陆失败")
    except:
        traceback.print_exc()




