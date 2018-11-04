import requests
import unittest
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

from com.huicewang.day6.CheckPoint import CheckPoint


class DemoApi(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        response = None
        url = urljoin(self.base_url, 'login')
        data = {'username': username, 'password': password}
        try:
            response = requests.post(url, data=data)
        except:
            pass
        return response

    def get_cookies(self, username, password):
        return self.login(username, password).cookies

    def info(self, cookies):
        url = urljoin(self.base_url, 'info')

        return requests.get(url, cookies=cookies).json()


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_url = 'http://127.0.0.1:5000'
        cls.username = 'admin'
        cls.password = '123456'
        cls.app = DemoApi(cls.base_url)

    def test_login(self):
        response = self.app.login(self.username, self.password).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'

    def test_info(self):
        cookies = self.app.get_cookies(self.username, self.password)
        response = self.app.info(cookies)
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'