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
        'cookie': 'CGIC=EhQxQzVHQ0VBX2VuX184NzhfXzg3OCJ8dGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2Uvd2VicCxpbWFnZS9hcG5nLCovKjtxPTAuOCxhcHBsaWNhdGlvbi9zaWduZWQtZXhjaGFuZ2U7dj1iMztxPTAuOQ; HSID=A-xCmu7jyU-SBRKrb; SSID=AiXdn0iE7s9ei3P_Y; APISID=WCEu2H_do8vcMoqf/ACRK4P-ugQ8jhuuZy; SAPISID=YamU6o-ltj89kvTX/AJsTBA7IVt68kFLC9; __Secure-3PAPISID=YamU6o-ltj89kvTX/AJsTBA7IVt68kFLC9; __Secure-HSID=A-xCmu7jyU-SBRKrb; __Secure-SSID=AiXdn0iE7s9ei3P_Y; __Secure-APISID=WCEu2H_do8vcMoqf/ACRK4P-ugQ8jhuuZy; ANID=AHWqTUlQ_rEko78Sv_o8fDHrT1_h84Em9FBXyNx8mtXdwaUpTFxO8r9S3xCXv09B; SEARCH_SAMESITE=CgQIoI8B; SID=uwczmGRSKwUP9BDVsaglhJbQxBLN5HbfwiKAM6LlZwOjjJNRziyctXd1HOxeai7gZJECSA.; __Secure-3PSID=uwczmGRSKwUP9BDVsaglhJbQxBLN5HbfwiKAM6LlZwOjjJNRojByC2eVaq40Hd5z3_IS8A.; NID=202=POEcoY2ezDWlgMXpQ6-U1UwzKXOmrw29iSVlg0moQpW-HLKuJRLLBVqSTV_xRErn-9lHj7Xy1AyIVqrmRevOTjpwEO3C3iOrI8n3ovMMTnmcvZ96U9GHaLx_zFOGlc0Z7NdGTVzSqMOI1-TJax1xoKsFlMNwpGoyzfTVEI4ODGiwR5A6AQcT_7cyTtALR61vjAnhpLXWbzYkNnxLCWvlSoLoNScoVc7QxKP4WPbTNtVMWAWAaxtBavov9XBnMI-B4iPmbA; DV=Q1EpEx0ytCJK4B5gABCykxFV_49xFlf4WvFgpuJ_GgUAABAgbgrVr3R9dwEAAFTcWbHAZMzfZwAAAA; 1P_JAR=2020-04-11-02; SIDCC=AJi4QfGcpjKwO5_Dc8ZXmTlLh7H7oPWuh_YvhxAESSby6Rfie3gLTnAvha3MI1opy2n9uMN2cQ'
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
