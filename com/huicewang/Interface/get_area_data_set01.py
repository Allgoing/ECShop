import unittest

import requests

from com.huicewang.day6.ExcelParser import ExcelParser


class InterfaceTest(unittest.TestCase):

    ep = ExcelParser(r'G:\接口用例.xlsx')

    def test_case01(self):

        url = 'https://www.zgjky.cn/webservice/wtWebApiH/GetAuthService'
        data = {'userName': '13581515304', 'password': '1234qwer.', 'userType': '1', 'adCode': '110101'}
        r = requests.post(url, data=data, verify=False).json()
        self.token = r['token']
        # print(r.json())

        url = 'https://www.zgjky.cn/webservice/wtWebApiH/GetServerData'
        data1 = {'token': self.token,
                 'infoType': '660100',
                 'jsonValue': '{"page":"1","rows":"10","docType":"","orderType":"","lat":"39.918378","lon":"116.415364",'
                             '"serviceWay":"","ignoreLogin":1}'}

        response = requests.post(url, data=data1, verify=False)
        print(response.json())

