#!/usr/bin/python
#coding: utf-8

import datetime
import pymongo
import sys
import re
import requests
from lxml import etree
import codecs
from bs4 import BeautifulSoup
from get_stitle import gettitles
from get_spublish_time import getpublish_time
from process import for_time

def str2datetime(time_str):
    #匹配的time_str，会有空格，导致后面strptime出错
    time_str = time_str.strip()
    time_format = ''
    if time_str.find('/') >0:
        if time_str.find(':') >0:
            time_format = "%Y/%m/%d %H:%M:%S"
        else:
            time_format = "%Y/%m/%d"
    elif time_str.find(':') == -1:
        time_format = "%Y-%m-%d"
    elif time_str.count(':') ==1:
        time_format = "%Y-%m-%d %H:%M"
    else:
        time_format = "%Y-%m-%d %H:%M:%S"
    try:
        pub_time = datetime.datetime.strptime(time_str, time_format)
    except:
        pub_time = ''
    return pub_time

def get_publish_times(html):
    xpath = getpublish_time(html)
    if xpath == '':
        return get_publish_time(html.text)
    if html.text =='' or html.text == None:
        return get_publish_time(html.text)
    try:
        tree = etree.HTML(html.text)
        if tree == None or tree == '':
            return get_publish_time(html.text)
        dom = tree.xpath(xpath)
    except:
        dom = ''
    txt = ''
    for item in dom:
        txt +=item.strip()
#        break
    if txt=='':
       return  get_publish_time(html.text)
    elif re.match(ur'.*[\u4e00-\u9fa5]{1,}.*',txt):
        match = re.search('(\d{4}-\d{1,2}-\d{1,2})',txt)
        if match:
            return str2datetime(match.group(1))
        match = re.search(u'(\d{4})年(\d{1,2})月(\d{1,2})日', txt)
        if match:
            year = int(match.group(1))
            month = int(match.group(2))
            day = int(match.group(3))
            return datetime.datetime(year, month, day)
        return  get_publish_time(html.text)
    else:
        return str2datetime(txt)

def get_publish_time(text):
    return for_time(text)
    
"""
    match = re.search('(\d{4}-\d{1,2}-\d{1,2})',text)
    if match:
        return str2datetime(match.group(1))
"""
    #若都没有匹配到，返回空
#根据tree正文提取

def get_titles(html):
    xpath = gettitles(html)
    if xpath == '':
        return get_title(html.text)
    if html.text ==''  or html.text == None:
        return get_title(html.text)
    try:
        global coding
        tree = etree.HTML(html.text)
        if tree == None or tree == '':
            return get_title(html.text)
        dom = tree.xpath(xpath)
    except:
        return get_title(html.text)
    txt = ''
    for item in dom:
        if re.search(r'^\|$',item.strip()):
            continue
        txt +=item.strip()
        if txt !='':
            break
    if txt=='':
       return  get_title(html.text)
    else:
        return txt

#根据title标签提取
def get_title(text):
    #beautifulsoup获取标签
    soup = BeautifulSoup(text[text.find(">")+1:])
    try:
        title = soup.title.string.strip() if soup.title else ''
    except AttributeError:
        title = ''
    
    #url = 'http://www.ls12365.gov.cn/www/zjgk/979.htm'
    #处理这个网站
    title = re.sub(u'^::', '', title)
    title = re.sub(u'::$', '', title)
    if title.find('_') >= 0:
        title = title.split('_',1)
        titles = re.search(u'\S+(市|省|州|区|质量|信息|技术|工商)\S*(网|局|网站)$',title[1])
        if titles:
            title = title[0].strip('_')
        else:
            title = title[1].strip('_')
    elif title.find('-') >=0:
        if re.search(ur'江门市质量技术监督局',title):
            return title.split('-')[1]
        title = title.split('-',1)
        if re.search(' Powered by',title[1]):
            return title[0]
        titles = re.search(u'\S+(市|省|州|区|质量|技术|信息|工商|金质|网站群)\S*(网|局|网站)$',title[1])
        if titles:
            title = title[0].strip('-')
        else:
            title = title[1].strip('-')
    elif title.find('|') >= 0:
        title = title.split('|',1)
        titles = re.search(u'\S+(市|省|州|区|质量|技术|工商)\S*(网|局|网站)$',title[1])
        if titles:
           title = title[0].strip('|')
        else:
           title = title[1].strip('|')
    elif title.find('>>') >=0:
        title =title.split('>>',1)
        titles = re.search(u'\S+(市|省|州|区|质量|技术|工商)\S*(网|局|网站)$',title[1])
        if titles:
            title = title[0].strip('>')
        else:
            title = title[1].strip('>')
    elif title.find(' ') >=0:
        title =title.split(' ',1)
        titles = re.search(u'\S+(市|省|州|区|质量|技术|信息|工商)\S*(网|局|网站)$',title[1])
        if titles:
            title = title[0].strip()
        else:
            title = title[1].strip()
    elif title.find(ur'－') >=0:
        title = title.split(ur'－',1)
        titles = re.search(u'\S+(市|省|州|区|工商|质量|技术|信息|金质)\S*(网|局|网站)$',title[1])
        if titles:
            title = title[0]
        else:
            title = title[1]

    return title
