#!/home/sdu/tools/python3/venv/bin/python
import os
import sys
sys.path.append(os.getcwd())

import re
import requests

from datetime import datetime
from utils.convert.date import (datetime_to_strtime)
from utils.notices import (send_ding)


def req(keywords):
    url = 'https://www.google.com/search'
    params = {
        'newwindow': '1',
        'rlz': '1C5GCEA_en__878__878',
        'biw': '1440',
        'bih': '373',
        'tbs': 'sbd:1',
        'tbm': 'nws',
        'sxsrf': 'ALeKk00pKiHPP9_NQNxfSso_PomF3xeADg:1587299177055',
        'ei': 'aUOcXvD-AtOlwAOYiJXICw',
        'q': keywords,
        'oq': keywords,
        'gs_l': 'psy-ab.12...0.0.0.12300.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.QNoZ5iGbzc4',

    }
    headers = {
        'authority': 'www.google.com', 
        'dpr': '2', 
        'upgrade-insecure-requests': '1', 
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36', 
        'sec-fetch-dest': 'document', 
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
        'x-client-data': 'CKC1yQEIhrbJAQiltskBCMG2yQEIqZ3KAQiroMoBCMuuygEI0K/KAQi8sMoBCJe1ygEI7bXKAQiOusoBGLy6ygE=', 
        'sec-fetch-site': 'same-origin', 
        'sec-fetch-mode': 'navigate', 
        'sec-fetch-user': '?1', 
        'referer': 'https://www.google.com/', 
        'accept-language': 'zh-CN,zh;q=0.9', 
        'cookie': 'ANID=AHWqTUkYfaABtlgXyY-P6eQM1awbRA0B1gzkotUVknun7GbjZixFm6LZoEKk79Zi; HSID=AFnAbf-RtCr4W1Lxk; SSID=AC7OOzDfPFXLB-izR; APISID=YErsp46CuFs3k55a/AKPPoTJCUH8CjHlgY; SAPISID=KuJL-2sZG8HQn2ey/AdtPt-erke5-8Nc5i; __Secure-HSID=AFnAbf-RtCr4W1Lxk; __Secure-SSID=AC7OOzDfPFXLB-izR; __Secure-APISID=YErsp46CuFs3k55a/AKPPoTJCUH8CjHlgY; __Secure-3PAPISID=KuJL-2sZG8HQn2ey/AdtPt-erke5-8Nc5i; CONSENT=YES+JP.zh-CN+20180610-19-0; SID=xQemJ_QaGxTq-2bvOG-v-mYeC62QMiDgFQPaCZFlMjG7hZ-xnHqGBSdHvoD-P9l2Y9Hedw.; __Secure-3PSID=xQemJ_QaGxTq-2bvOG-v-mYeC62QMiDgFQPaCZFlMjG7hZ-xyqPquCvhk1vsVihDnHH_vQ.; SEARCH_SAMESITE=CgQI648B; NID=204=pgEzL6BmENqLEaFKMwKPTZ7rkEciX0M_IAxFciiFacE8Paaf3zkFRi0o_OYfbdzdRFA9wptMXadu1TC-y77vc2Q-RYzVzoXjEiHNTgFPrGoRYw94cwoJmahAlpot03JO32zvYtEDrambBciUFyLnK8O96IWQx9KtxwG1Ww7yeGN5JRJJEKiPJW6D3KTencyhnFAdK1Js29JX6klduhudC24wMMjhWu7o-C7-; 1P_JAR=2020-05-29-11; SIDCC=AJi4QfESmew_46yp-VOIbwfndHPSUG8PCfpqZBrZpC4glFYQE8IXRdfLZnCgRTk2KW8N4rotFO4'
    }

    resp = requests.get(url=url, params=params, headers=headers)
    print(resp.status_code)
    return resp.text

def parse(content):
    found_strs = re.compile(r'</style><div id="taw">(.*?)<div id="bottomads"></div>').findall(content)
    if found_strs:
        found_strs = found_strs[0]

    found_strs = found_strs.replace(' ', '')
    found_hrefs = re.compile(r'<aclass="......"href="(.*?)"ping="/url\?sa=t&amp;source=web&amp;rct=j&amp;url=').findall(found_strs)
    found_titles = re.compile(r'target="_blank"rel="noopener">(.*?)</a></h3><divclass=".*?">').findall(found_strs)
    found_contents = re.compile(r'</div><divclass="st">(.*?)</div></div></div></div><divclass="g">').findall(found_strs)
    found_authers = re.compile(r'<divclass=".*?"><spanclass=".*?">(.*?)</span>').findall(found_strs)

    messages = "Google News: {} \nPast 24 hours, Sorted By date, Top 5 \n{} \n".format(
        datetime_to_strtime(datetime.now()),
        '-'*30,
    )
    count = 1
    for href, title, content, auther in zip(found_hrefs, found_titles, found_contents, found_authers):
        if len(title.split('target="_blank"rel="noopener">')) > 1:
            title = title.split('target="_blank"rel="noopener">')[1] 
        title = title.replace('&quot;', '').replace('<em>', '').replace('</em>', '')
        content = content.replace('&quot;', '').replace('<em>', '').replace('</em>', '')

        messages += "Title: {} \nAuther: {} \nUrl: {} \n{} \n".format(
            title, auther, href,
            '-'*30,
        )
        count += 1
        if count > 5 :
            break

    return messages
    
def oil_news():
    keywords = '石油 沙特 | 石油 期货'
    resp_text = req(keywords)
    messages = parse(resp_text)
    print(messages)

    token = '6079179bc90326ec71a3700f7d5c483e5441625c70a878494de966fc420bff47'
    send_ding(token, messages)

def epidemic_news():
    keywords = '疫情 趋势 全球'
    resp_text = req(keywords)
    messages = parse(resp_text)
    print(messages)

    token = '92f61d5b2cbc46d66458c95b93e86b264206f54adfdb135aac247f3ef704e7b0'
    send_ding(token, messages)

def gold_news():
    keywords = '黄金 避险'
    resp_text = req(keywords)
    messages = parse(resp_text)
    print(messages)

    token = 'ad6d0a953401c8ce734c7079615a0e54f71bd79c3866d495ab1fe336594ed0ba'
    send_ding(token, messages)

def main():
    '''
    0 6-22/1 * * * cd /home/sdu/tools/python3; venv/bin/python google_news/crawler.py oil >> google_news/crawler.log 2>&1 & 
    20 6-22/2 * * * cd /home/sdu/tools/python3; venv/bin/python google_news/crawler.py gold >> google_news/crawler.log 2>&1 & 
    40 6-22/3 * * * cd /home/sdu/tools/python3; venv/bin/python google_news/crawler.py epidemic >> google_news/crawler.log 2>&1 & 
    '''
    args = sys.argv[-1]
    if args == 'oil':
        oil_news()

    if args == 'epidemic':
        epidemic_news()
    
    if args == 'gold':
        gold_news()

if __name__ == "__main__":
    main()

