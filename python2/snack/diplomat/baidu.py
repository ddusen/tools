#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')

import re

import datetime
import time
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
        url = 'http://m.baidu.com/appsrv?usertype=0&cen=cuid_cut_cua_uid&abi=armeabi-v7a&action=getcommentlist&pkname=com.baidu.appsearch&province=q8vJklO_etgCRS886OSCkjuJeug_RBuRodkqA&native_api=1&gms=true&from=1009556z&cct=q8vJk0iteuggRH8y6iv3kjO_eag_MHf3odfqA&pu=ctv%401%2Ccfrom%401009556z%2Ccua%40_avLCgaH-i46ywoUfpw1z4aBsiz0aX8b4a2AiqqHB%2Ccuid%400aB180uZ2alGuHaJjaSaiYapSi__82ayli2IfYakH86WuviJ0av-iguKBi_7u28q_uBqtqqqB%2Ccut%40yk268_ujL8o0uD8bgNmU6fJsx6N7gqqSB%2Cosname%40baiduappsearch&network=WF&operator=&psize=3&country=CN&is_support_webp=true&cll=ga2iNgaq28gTueiyla2LNgudvt3NSqqqB&uid=0aB180uZ2alGuHaJjaSaiYapSi__82ayli2IfYakH8qDuHivguvn8jaV2i_Sa2iqsTqqC&language=zh&apn=&platform_version_id=22&ver=16792523&&crid=1489117696094&native_api=1&actiontype=getCommentList&groupid=4620376&start='+ str(page) +'&count=10&docid=11099331&packageid=1522061&groupids=4620376%404559739%404501437%404477320%404373958%404278203%404113334%404068616%404062924%403965970%403937955&machine=XT1060&osversion=5.1&rqt=rty&ptl=hp'
        header = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
        }
        handle_data(get_response(url, headers=header).text)
        time.sleep(3)
        page += 10
        print page


def handle_data(source_data):
    data = eval(source_data)
    messages = data.get('data')
    for message in messages:
        username = message.get('reserved3').get('machine') + '机型用户'
        user_star = 0
        game_version = message.get('reserved3').get('version')
        content = (message.get('content').decode('unicode-escape')).encode('utf-8')
        create_at = datetime.datetime.fromtimestamp(int(message.get('create_time')) / 1e3)
        likes = int(message.get('like_count'))
        comment_number = int(message.get('reply_count'))
        model = message.get('reserved3').get('machine')
        weight = ""
        image_url = message.get('usericon')
        channel = 'baidu'

        # print (username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)
        if save(sql=u'''INSERT INTO `base_comment`(`username`, `user_star`, `game_version`, `content`, `create_at`, `likes`, `comment_number`, `model`, `weight`, `image_url`, `channel`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s) ''', list1=(username, user_star, game_version, content, create_at, likes, comment_number, model, weight, image_url, channel)):
            print "INSERT INTO < %s > SUCCESSFUL!" % username


def main():
    get_data()

if __name__ == '__main__':
    main()
