import shutil
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner

import time

from com.huicewang.day6.EMail import EMail
from com.huicewang.day6.XmlParser import XmlParser


if __name__ == '__main__':
    parser = XmlParser('E:\config.xml')
    test_dir = parser.get_element_text('.//case_path')
    pattern = parser.get_element_text('.//case_pattern')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern=pattern)
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    with open(r'E:\report\history\\' + now + '.html', 'wb') as fp:
        HTMLTestRunner(fp, title='ECShop测试报告', description='lisi').run(discover)
    shutil.copy(r'E:\report\history\\' + now + '.html', r'E:\report\index.html')

    smtp_server = parser.get_element_text('./mail/SMTPserver')
    from_addr = parser.get_element_text('./mail/from')
    from_pwd = parser.get_element_text('./mail/password')
    to_addrs = parser.get_element_text('./mail/to')
    copy_to = parser.get_element_text('./mail/copyTo')
    file_path = parser.get_element_text('./mail/filename')
    subject = parser.get_element_text('./mail/subject')
    email = EMail(smtp_server, from_addr, from_pwd, to_addrs, file_path, subject, copy_to)
    email.send_mail()

