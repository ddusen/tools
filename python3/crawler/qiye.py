import requests
import random

def main():
    params = {
        'mobileAction': 'entSearch',
        'keywords': '百度',
        'topic': 1,
        'pageNum': 1,
        'pageSize': 10
        # 'userID': 'id001',
        # 'userIP': '192.123.123.13'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.1; E6683 Build/32.4.A.1.54; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Html5Plus/1.0'
    }
    # http://www.kuaidaili.com/free/
    proxies = (
                {'http': 'http://121.232.145.148:9000'},
                {'http': 'http://122.96.59.102:80'},
                {'http': 'http://60.214.154.2:53281'},
                {'http': 'http://121.232.147.81:9000'},
            )

    r = requests.post('http://yd.gsxt.gov.cn/QuerySummary',
                      headers=headers, 
                      proxies=proxies[random.randint(0, 3)], 
                      data=params)

    print(r.content)


if __name__ == '__main__':
    main()
