#!/usr/bin/env python3
# encoding: utf-8

"""
@author: aaa
@file: eakay.py
@time: 2018/5/19 9:11
@desc:
"""


import requests
import threading

def post_eakay():

    r = 0
    url = 'http://wx.cnevi.com/app/index.php?i=3&c=entry&rid=20&id=37&do=vote&m=tyzm_diamondvote '
    headers = {'Host': 'wx.cnevi.com',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Language': 'zh-cn',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'http://wx.cnevi.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN',
            'Referer': 'http://wx.cnevi.com/app/index.php?i=3&c=entry&rid=20&id=37&do=view&m=tyzm_diamondvote&from=singlemessage&isappinstalled=0',
            'Cookie': 'PHPSESSID=6c6dfdcce7208218670b0eac5a79b5fa; Hm_lpvt_08c6f5e17c0761a968c5658ccf6ff5ad=1526691136; Hm_lvt_08c6f5e17c0761a968c5658ccf6ff5ad=1526691136'
              }
    data = {'latitude': 0,
            'longitude': 0,
            'verify': 0
            }

    for i in range(1000):
        r = requests.post(url, data=data, headers=headers).text
        print(r)
        # if r is 200:
        #     print('第%s次投票成功' % i)
        # else:
        #     print('第%s次投票失败' % i)


if __name__ == '__main__':
    post_eakay()

    # for i in range(20):
    #     thread = threading.Thread(target=post_eakay)
    #     thread.start()

