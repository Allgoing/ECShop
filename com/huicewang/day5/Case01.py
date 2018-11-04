from com.huicewang.day3 import DriverFactory
from com.huicewang.day5.NewApi import NewApi

if __name__ == '__main__':
    driver = DriverFactory.create_driver('firefox')
    api = NewApi(driver, './config.xml')
    api.to('http://www.huicewang.com/ecshop/index.php')
    api.click('首页', '登录按钮')
    api.wait(2)
    api.send_keys('登录页', '用户名', 'zach')
    api.send_keys('登录页', '密码', '123456')
    api.click('登录页', '登录按钮')
    api.wait(5)

    try:
        if api.elements_text('首页', '登录标示') == 'zach':
            print('登陆成功')
        else:
            print('登陆失败1')
    except:
        print('登陆失败2')
    finally:
        api.close()