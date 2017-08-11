#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')

import re

from datetime import datetime
from lxml import etree, html

from mysql import query, query_one, save

from process import (extract_content_by_xpath,
                                                 extract_link_by_re,
                                                 extract_pubtime_by_re,
                                                 extract_item_by_re,
                                                 extract_title_by_xpath,
                                                 get_response, is_last_node,
                                                 get_max_page_number)


def get_data():
    page = 0
    while(True):
        url = 'http://comment.mobilem.360.cn/comment/getComments?baike=3073428&level=0&start=%s&count=10&topLike=1&os=22&vc=300070026&v=7.0.26&md=XT1060&sn=4.391372128381046&cpu=msm8960dt&ca1=armeabi-v7a&ca2=armeabi&m=70b45cdc762b8a01062cd7e18d92d81b&m2=05e078182db0ed99fac82e9df42df316&ch=8294092&ppi=720_1184&startCount=1&re=1200&tid=0&cpc=1&snt=-1&nt=1&gender=-1&age=-1&theme=2&br=motorola&s_3pk=1&webp=1' % page
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        }
        handle_data(get_response(url, headers=header).text)
        time.sleep(3)
        page += 10
        print page


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
        channel = '360'

        # print (username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)
        if save(sql=u'''INSERT INTO `base_comment`(`username`, `user_star`, `game_version`, `content`, `create_at`, `likes`, `comment_number`, `model`, `weight`, `image_url`, `channel`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s) ''', list1=(username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)):
            print "INSERT INTO < %s > SUCCESSFUL!" % username


def main():
    get_data()

if __name__ == '__main__':
    main()
