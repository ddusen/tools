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
    page = 0
    while(True):
        url = 'http://comment.wandoujia.com/comment/comment!getCommentSummary.action?pageNum=%s&pageSize=15&target=com.tencent.tmgp.sgame' % page
        page += 1
        handle_data(get_response(url).text)


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
