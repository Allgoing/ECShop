# from selenium.webdriver.firefox import webdriver
# 前端页面性能数据分析
import time
from selenium import webdriver

if __name__ == '__main__':
    fp = webdriver.FirefoxProfile()
    fp.add_extension(r'E:\root\firebug-2.0.17.xpi')
    fp.add_extension(r'E:\root\netExport-0.8.xpi')
    fp.set_preference('extensions.firebug.allPagesActivation', 'on')
    fp.set_preference('extensions.firebug.defaultPanelName', 'net')
    fp.set_preference('extensions.firebug.net.enableSites', 'true')
    fp.set_preference('extensions.firebug.netexport.alwaysEnableAutoExport', 'true')
    fp.set_preference('extensions.firebug.netexport.autoExportToFile', 'true')
    fp.set_preference('extensions.firebug.netexport.saveFiles', 'true')
    fp.set_preference('extensions.firebug.netexport.defaultLogDir', r'E:\logs')
    driver = webdriver.Firefox(firefox_profile=fp)

    time.sleep(4)
    driver.get("http://www.baidu.com")