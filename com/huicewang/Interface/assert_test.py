import requests


if __name__ == '__main__':

    login_url = r'https://www.zgjky.cn/webservice/wtWebApiH/GetAuthService'
    data = {'userName': '13581515304',
            'password': '1234qwer.',
            'userType': '1',
            'adCode': '110118'
    }
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = requests.post(login_url, data=data, headers=header, verify=False).json()
    token = response['token']

    login_url1 = r'https://www.zgjky.cn/webservice/wtWebApiH/GetServerData'
    data1= {'token': token,
            'infoType':	'111180',
            'jsonValue': '{"page":1,'
                         '"rows":20,'
                         '"platType":"2",'
                         '"ignoreLogin":"1",'
                         '"sortDictType":"1",'
                         '"d.serviceDictScopeCode":"11000000",'
                         '"serviceDictScopeLevel":"1"}'
            }
    response1 = requests.post(login_url1, data=data1, headers=header, verify=False).json()
    print(response1['rows']['eaName'])




