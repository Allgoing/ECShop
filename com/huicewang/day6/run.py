import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

import time

from com.huicewang.day6.XmlParser import XmlParser


if __name__ == '__main__':
    parser = XmlParser('E:\config.xml')
    test_dir = parser.get_element_text('.//case_path')
    pattern = parser.get_element_text('.//case_pattern')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    with open(r'E:\report\\' + now + '.html', 'wb') as fp:
        HTMLTestRunner(fp, title='ECShop测试报告', description='lisi').run(discover)