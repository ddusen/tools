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
        url = 'http://comment.wandoujia.com/comment/comment!getCommentSummary.action?pageNum=%s&pageSize=15&target=com.tencent.tmgp.sgame' % page
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        }
        handle_data(get_response(url, headers=header).text)
        time.sleep(3)
        page += 1
        print page


def handle_data(source_data):
    source_data = source_data.replace('false', 'False')
    source_data = source_data.replace('true', 'True')
    messages = eval(source_data).get('comments')
    for message in messages:
        username = message.get('authorName')
        user_star = 5 if message.get('enjoy') == 'True' else 1
        game_version = ""
        content = message.get('content')
        create_at = message.get('date')
        likes = int(message.get('agreeCount'))
        comment_number = 0
        model = ""
        weight = 0
        image_url = message.get('avatar')
        channel = 'wandoujia';
        # print (username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)
        if save(sql=u'''INSERT INTO `base_comment`(`username`, `user_star`, `game_version`, `content`, `create_at`, `likes`, `comment_number`, `model`, `weight`, `image_url`, `channel`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s) ''', list1=(username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)):
            print "INSERT INTO < %s > SUCCESSFUL!" % username


def main():
    get_data()

if __name__ == '__main__':
    main()
