import time
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

from com.huicewang.day5.XmlParser1 import XmlParser

if __name__ == '__main__':
    parser = XmlParser('G:\config.xml')
    test_dir = parser.get_element_text('.//case_path')
    pattern = parser.get_element_text('.//case_pattern')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    # unittest.TextTestRunner().run(discover)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    with open(r'E:\report\\'+now+'.html', 'wb') as fp:
        HTMLTestRunner(fp, title='report.html', description='xxxx').run(discover)
        # runner = HTMLTestRunner(fp, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
