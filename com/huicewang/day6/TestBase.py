import unittest

from com.huicewang.day6 import DriverFactory, CheckPoint
from com.huicewang.day6.NewApi import NewApi


class TestBase(unittest.TestCase):
    driver = None
    api = None

    @classmethod
    def setUpClass(cls):
        driver = DriverFactory.create_driver('firefox')
        cls.api = NewApi(driver, 'E:\config.xml')

    @classmethod
    def tearDownClass(cls):
        cls.api.close()

    def setUp(self):
        self.check = CheckPoint.CheckPoint()
        self.api.to('http://www.huicewang.com/ecshop/index.php')

    def tearDown(self):
        self.api.to('www.huicewang.com/ecshop/user.php?act=logout')

