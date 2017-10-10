#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re
import time
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')

from mysql import query, query_one, save
from process import (get_response, HandleContent, clear_space)
from readability import Readability

headers = {
    'User-Agent': 'Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Cookie': 'BAIDUID=3FA69E29AFE31D75577B34CAE676D9C5:FG=1; BIDUPSID=471359EB508C0D86D13E3E7D4D65BB51; PSTM=1495077531; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; MCITY=-%3A; LOCALGX=%u6B66%u6C49%7C%34%38%31%32%7C%u6B66%u6C49%7C%34%38%31%32; Hm_lvt_e9e114d958ea263de46e080563e254c4=1495588628,1495592348,1495700854,1495760429; H_PS_PSSID=; BD_CK_SAM=1; BDSVRTM=82; Hm_lpvt_e9e114d958ea263de46e080563e254c4=1495764288; PSINO=1; BDRCVFR[C0p6oIjvx-c]=mk3SLVN4HKm; pgv_pvi=8960308224; pgv_si=s1673304064'
}
__re = {
    'url': re.compile(r'<h3 class="c-title"><a href="(.*?)"'),
    'source_pubtime': re.compile(r'<p class="c-author">(.*?)&nbsp;&nbsp;(...........) ..:..</p>'), 
    'encoding': re.compile(r'content="text/html; charset=(.*?)"')
}

flag = 0
count = 0

def get_enterprise_name():
    return map(lambda x:x.get('name'), query(sql=u'SELECT `name` FROM `base_enterprise`'))


def get_response_custom(request_url):
    request_url = request_url
    try:
        html_doc = get_response(url=request_url, headers=headers).text
        encoding = __re.get('encoding').findall(html_doc)
        if not encoding:
            return html_doc
        elif encoding == u'utf-8':
            return html_doc
        else:
            return get_response(url=request_url, encoding=encoding[0], headers=headers).text
    except Exception as e:
        global flag
        flag += 1
        if flag > 5:
            flag = 0
            return ''
        print e
        time.sleep(2)
        get_response_custom(request_url)
        

def get_pages(html_doc):
    pages = re.compile(r'<a href="/ns\?word=.*?&pn=(.*?)&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0"><span')
    return pages.findall(html_doc)

def get_second_crawler_urls_pubtimes(html_doc):
    urls = __re.get('url').findall(html_doc)
    source_pubtime = __re.get('source_pubtime').findall(html_doc)
    return zip(urls, source_pubtime)

def save_data(first_html_doc, enterprise_name):
    second_crawler_request_urls_pubtimes = get_second_crawler_urls_pubtimes(first_html_doc)

    for second_crawler_request_url, source_pubtime in second_crawler_request_urls_pubtimes:
        if query_one(sql=u'SELECT COUNT(*) FROM `base_news` WHERE `url` = %s', list1=(second_crawler_request_url, )).get('COUNT(*)'):
            continue

        second_crawler_html_doc = get_response_custom(request_url=second_crawler_request_url)
        time.sleep(1)

        soup = Readability(second_crawler_html_doc, second_crawler_request_url)
        content = soup.content.strip()
        title = soup.title.strip()
        pubtime = source_pubtime[1]
        pubtime = pubtime.replace(u'年', u'-')
        pubtime = pubtime.replace(u'月', u'-')
        pubtime = pubtime.replace(u'日', u'-').strip()
        source = source_pubtime[0].strip()

        save(sql=u'INSERT INTO `base_news`(`title`, `url`, `content`, `pubtime`, `source`, `keyword`, `status`) VALUES(%s, %s, %s, %s, %s, %s, 0)', list1=(title, second_crawler_request_url, content, pubtime, source, enterprise_name))
        

def handle(enterprise_name):
    request_url_set = []
    request_url = 'http://news.baidu.com/ns?word=%s&pn=0&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0' % enterprise_name
    html_doc = get_response_custom(request_url=request_url)
    time.sleep(1)
    pages_number = get_pages(html_doc)
    if not pages_number:
        save_data(html_doc, enterprise_name)
    else:
        for page in pages_number:
            request_url_set.append(request_url)
            save_data(html_doc, enterprise_name)

            request_url = 'http://news.baidu.com/ns?word=%s&pn=%s&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0' % (enterprise_name, page)
            html_doc = get_response_custom(request_url=request_url)

            time.sleep(1)
            if request_url in request_url_set:
                break


def main():
    enterprise_name_list = get_enterprise_name()
    for enterprise_name in enterprise_name_list:
        global count
        count += 1
        print count, enterprise_name
        try:
            handle(enterprise_name)
        except Exception as e:
            print e
            time.sleep(3)
            continue
            
if __name__ == '__main__':
    main()
