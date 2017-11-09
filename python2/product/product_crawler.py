#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')
import time
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

"""
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `code` varchar(255) NOT NULL,
  `level` bigint(20) NOT NULL,
  `parent_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `product_parent_id_4925902a_fk_product_id` (`parent_id`),
  CONSTRAINT `product_parent_id_4925902a_fk_product_id` FOREIGN KEY (`parent_id`) REFERENCES `product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

header = {
    'Cookie': '_gscu_1771678062=93019765gxzmln75; _gscbrs_1771678062=1; _trs_uv=23e1_6_j1vtf47y; AD_RS_COOKIE=20083361',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
}


def handle_data(data, level, parent_id):
    for i in data:
        i_split_list = i.split('-')
        code = i_split_list[0]
        name = i_split_list[1]
        if save(sql=u"INSERT INTO `product`(`name`, `level`, `parent_id`, `code`) VALUES(%s, %s, %s, %s)", list1=(name, level, parent_id, code,)):
            print "INSERT PRODUCT< %s > SUCCESS!" % name


def handle_data_two(data, level, parent_id):
    for i in data:
        code = i[0]
        name = i[1]
        if save(sql=u"INSERT INTO `product`(`name`, `level`, `parent_id`, `code`) VALUES(%s, %s, %s, %s)", list1=(name, level, parent_id, code,)):
            print "INSERT PRODUCT< %s >, LEVEL< %s > SUCCESS!" % (name, level)


def level_one():
    page = 0
    while page < 5:
        if page == 0:
            url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/index.html'
        else:
            url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/index_%s.html' % page

        html_data = extract_item_by_re(get_response(
            url, headers=header).text, r'<font class="cont_tit03">(.*?)</font><font class="cont_tit02">')

        handle_data(data=html_data, level=1, parent_id=None)
        time.sleep(1)
        page += 1

    return True


def level_two():
    level_one_tuple = query(
        sql=u"SELECT `id`, `code` FROM product WHERE level = 1")
    for i in level_one_tuple:
        code = str(i.get('code'))
        sql_id = i.get('id')

        request_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/2010/%s.html' % code
        print request_url

        def excute():
            try:
                html_data = extract_item_by_re(get_response(url=request_url, encoding='gb2312', headers=header).text,
                                               r"<tr class='citytr'><td><a href='../....\.html'>(.*?)</a></td><td><a href='../....\.html'>(.*?)</a></td></tr>")
            except Exception as e:
                print e
                time.sleep(3)
                excute()

            return html_data

        handle_data_two(data=excute(), level=2, parent_id=sql_id)
        time.sleep(1)

    return True


def level_three():
    level_one_tuple = query(
        sql=u"SELECT `id`, `code` FROM product WHERE level = 1")
    for i in level_one_tuple:
        code_one = str(i.get('code'))
        id_one = i.get('id')
        level_two_tuple = query(
            sql=u"SELECT `id`, `code` FROM product WHERE level = 2 AND parent_id = %s ", list1=(id_one, ))
        for j in level_two_tuple:
            code_two = str(j.get('code'))
            id_two = j.get('id')

            request_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/2010/%s/%s.html' % (
                code_one, code_two)
            print request_url

            html_data = extract_item_by_re(get_response(url=request_url, encoding='gb2312', headers=header).text,
                                           r"<tr class='countytr'><td><a href='../(......)\.html'>.*?</a></td><td><a href='../......\.html'>(.*?)</a></td></tr>")
            handle_data_two(data=html_data, level=3, parent_id=id_two)
            time.sleep(1)

    return True


def level_four():
    level_one_tuple = query(
        sql=u"SELECT `id`, `code` FROM product WHERE level = 1")
    for i in level_one_tuple:
        code_one = str(i.get('code'))
        id_one = i.get('id')

        level_two_tuple = query(
            sql=u"SELECT `id`, `code` FROM product WHERE level = 2 AND parent_id = %s ", list1=(id_one, ))
        for j in level_two_tuple:
            code_two = str(j.get('code'))
            id_two = j.get('id')

            level_three_tuple = query(
                sql=u"SELECT `id`, `code` FROM product WHERE level = 3 AND parent_id = %s ", list1=(id_two, ))
            for k in level_three_tuple:
                code_three = str(k.get('code'))
                id_three = k.get('id')

                request_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/2010/%s/%s/%s.html' % (
                    code_one, str(code_two)[2:4:1], code_three)
                print request_url

                def excute():
                    try:
                        html_data = extract_item_by_re(get_response(url=request_url, encoding='gb2312', headers=header).text,
                                                       r"<tr class='towntr'><td><a href='../(........)\.html'>.*?</a></td><td><a href='../........\.html'>(.*?)</a></td></tr>")
                        if html_data == []:
                            html_data = extract_item_by_re(get_response(
                                url=request_url, encoding='gb2312', headers=header).text, r"<tr class='villagetr'><td>(.*?)</td><td>(.*?)</td>")
                    except Exception as e:
                        print e
                        time.sleep(3)
                        excute()

                    return html_data

                handle_data_two(data=excute(), level=4, parent_id=id_three)
                time.sleep(1)

    return True


def level_five():
    level_one_tuple = query(
        sql=u"SELECT `id`, `code` FROM product WHERE level = 1")
    for i in level_one_tuple:
        code_one = str(i.get('code'))
        id_one = i.get('id')

        level_two_tuple = query(
            sql=u"SELECT `id`, `code` FROM product WHERE level = 2 AND parent_id = %s ", list1=(id_one, ))
        for j in level_two_tuple:
            code_two = str(j.get('code'))
            id_two = j.get('id')

            level_three_tuple = query(
                sql=u"SELECT `id`, `code` FROM product WHERE level = 3 AND parent_id = %s ", list1=(id_two, ))
            for k in level_three_tuple:
                code_three = str(k.get('code'))
                id_three = k.get('id')

                level_four_tuple = query(
                    sql=u"SELECT `id`, `code` FROM product WHERE level = 4 AND parent_id = %s ", list1=(id_three, ))
                for x in level_four_tuple:
                    code_four = str(x.get('code'))
                    id_four = x.get('id')

                    request_url = 'http://www.stats.gov.cn/tjsj/tjbz/tjypflml/2010/%s/%s/%s/%s.html' % (code_one,  str(
                        code_two)[2:4:1],  str(code_three)[4:6:1], code_four)
                    print request_url

                    def excute():
                        try:
                            html_data = extract_item_by_re(get_response(
                                url=request_url, encoding='gb2312', headers=header).text, r"<tr class='villagetr'><td>(.*?)</td><td>(.*?)</td>")
                        except Exception as e:
                            print e
                            time.sleep(3)
                            html_data = extract_item_by_re(get_response(
                                url=request_url, encoding='gb2312', headers=header).text, r"<tr class='villagetr'><td>(.*?)</td><td>(.*?)</td>")
                            excute()

                        return html_data

                    handle_data_two(data=excute(), level=5, parent_id=id_four)
                    time.sleep(1)

    return True


def main():
    if level_one():
        if level_two():
            if level_three():
                if level_four():
                    if level_five():
                        print "EXCUTE SUCCESS!"


if __name__ == '__main__':
    main()
