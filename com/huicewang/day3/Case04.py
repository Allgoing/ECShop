from selenium import webdriver
import time
import json
import DriverFactory
from Login import Login
from Order import Order

if __name__ == '__main__':
    # pass
    driver = DriverFactory.creat_driver('ff')
    Login(driver).login('zach','123456')
    os = Order(driver).search('2017061119053')
    for o in os:
        print(o)
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.get('http://www.huicewang.com/ecshop/')
    # time.sleep(2)
    # driver.add_cookie({"name":"ECS[password]","value":"b3778dc5d587f8f152b76304724aa313"})
    # driver.add_cookie({"name": "ECS[user_id]", "value": "11"})
    # driver.add_cookie({"name": "ECS[username]", "value": "zach"})
    # driver.refresh()
    #
    # driver.get('http://www.huicewang.com/ecshop/user.php?act=order_list')
    # time.sleep(2)
    # try:
    #     trs = driver.find_elements_by_xpath("//div[@class='userCenterBox boxCenterList clearfix']/table/tbody/tr")
    #     order_number = len(trs)-1
    # except:
    #     order_number = 0
    #
    # if order_number > 0:
    #     orders = {}
    #     for i in range(1, len(trs)):
            # 写法一：利用连续findelement方法
            # tds = trs[i].find_elements_by_tag_name('td')
            # for j in range(0,len(tds)-1):
            #     if j==0:
            #         o_id =  tds[j].find_element_by_tag_name('a').text
            #         orders[o_id] = []
            #         continue
            #     orders[o_id].append(tds[j].text)

            # 写法二：利用xpath表达式拼接方法
            # tds = driver.find_elements_by_xpath("// div[@class ='userCenterBox boxCenterList clearfix']/table/tbody/tr["+str(i+1)+"]/td")
            # orders[tds[0].text] = [tds[1].text,tds[2].text,tds[3].text]

        # print(json.dumps(orders,ensure_ascii=False,encoding="gb2312"))