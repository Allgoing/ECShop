#!/usr/bin/env python3
# encoding: utf-8

"""
@author: aaa
@file: ceshi.py
@time: 2018/8/1 8:23
@desc:
"""

from selenium import webdriver
import requests


href_lists = []
driver = webdriver.Firefox()
driver.get('http://www.huanqiu.com/')
elements = driver.find_elements_by_xpath('//a')
for element in elements:
    href_lists.append(element.get_attribute('href'))

flag = 0
for url in href_lists:
    if url is None:
        print(url)
        break
    response = requests.get(url)
    result = response.status_code
    if result is not 200:
        print('url:%s打不开，状态码是%d' % (url, result))
        flag += 1

if flag == 0:
    print('连接正常')