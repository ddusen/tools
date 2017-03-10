#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
root_mod = '/home/sdu/MyProject/tools'
sys.path.append(root_mod)

import re

from datetime import datetime
from lxml import etree, html

from mysql import query, query_one, save

from tools.crawler.utils.crawler.process import (extract_content_by_xpath,
                                                 extract_link_by_re,
                                                 extract_pubtime_by_re,
                                                 extract_item_by_re,
                                                 extract_title_by_xpath,
                                                 get_response, is_last_node,
                                                 get_max_page_number)


def get_data():
    urls = ['http://comment.wandoujia.com/comment/comment!getCommentSummary.action?pageNum=0&pageSize=15&target=com.tencent.tmgp.sgame',
            'http://comment.mobilem.360.cn/comment/getComments?baike=3073428&level=0&start=0&count=10&topLike=1&os=22&vc=300070026&v=7.0.26&md=XT1060&sn=4.391372128381046&cpu=msm8960dt&ca1=armeabi-v7a&ca2=armeabi&m=70b45cdc762b8a01062cd7e18d92d81b&m2=05e078182db0ed99fac82e9df42df316&ch=8294092&ppi=720_1184&startCount=1&re=1200&tid=0&cpc=1&snt=-1&nt=1&gender=-1&age=-1&theme=2&br=motorola&s_3pk=1&webp=%s',
            'http://market.xiaomi.com/apm/comment/list/108048?channel=market_100_1_android&clientId=56df5d2d2eafff6a7366aa331b99ff14&co=CN&densityScaleFactor=2.0&imei=70b45cdc762b8a01062cd7e18d92d81b&la=zh&marketVersion=146&model=XT1060&os=1&page=1&resolution=720*1184&sdk=22&session=2jmj7l5rSw0yVb_v']

    page = 0
    while(True):
        url = urls[1] % page
        handle_data(get_response(url).text)
        page += 1


def handle_data(source_data):
    data = eval(source_data).get('data')
    messages = data.get('messages')
    for message in messages:
        username = (message.get('username').decode('unicode-escape')).encode('utf-8')
        user_star = int(message.get('score'))
        game_version = message.get('version_name')
        content = (message.get('content').decode('unicode-escape')).encode('utf-8')
        create_at = message.get('create_time')
        likes = int(message.get('likes'))
        comment_number = int(message.get('replies'))
        model = message.get('model')
        weight = message.get('weight')
        image_url = message.get('image_url')

        if save(sql=u'''INSERT INTO `base_comment`(`username`, `user_star`, `game_version`, `content`, `create_at`, `likes`, `comment_number`, `model`, `weight`, `image_url`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ''', list1=(username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url)):
            print "INSERT INTO < %s > SUCCESSFUL!" % username


def main():
    get_data()

if __name__ == '__main__':
    main()
