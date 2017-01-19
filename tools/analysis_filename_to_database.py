#!/usr/bin/python
# coding=utf-8

import os
import mysql

'''
	目标:
		分析文件目录, 得到所有文件名, 并添加到数据库.
	如下:
+-----+------------+---------------+------+----------+----------+---------+----------------------------+----------------------------+--------+---------+
| id  | app        | file          | rank | priority | interval | timeout | create_at                  | update_at                  | status | sub_app |
+-----+------------+---------------+------+----------+----------+---------+----------------------------+----------------------------+--------+---------+
|   1 | inspection | qhzljd        |    1 |        3 |     3600 |    3600 | 2016-06-15 03:06:28.051306 | 2016-06-15 03:06:28.051306 |      0 |         |
|   2 | inspection | qhzljd        |    2 |        3 |     3600 |    3600 | 2016-06-15 03:06:28.162080 | 2016-06-15 03:06:28.162080 |      0 |         |


'''
insert_sql = u"""INSERT INTO crawler.crawler_taskconf(app, `file`, rank, priority, `interval`, timeout, create_at, update_at, `status`, sub_app)VALUES(%s, %s, %s, 3, 3600, 3600, now(), now(), 1, '');"""


def get_file_list():
    # top_path = raw_input('请输入待查找的初始目录:')
    top_path = "/home/sdu/Project/crawler/common/crawler/service/apps/inspection/impl/"

    result = os.walk(top_path)
    for file in result:
        return file[2]


def main():
    file = get_file_list()
    for i in file:
        deal_with_file = i.split('.')

        file_name = deal_with_file[0]
        extension_name = deal_with_file[1]

        if extension_name == 'py':
            if file_name != '__init__':
                result1 = mysql.save(insert_sql, list1=(
                    'inspection', file_name, 1))
                result2 = mysql.save(insert_sql, list1=(
                    'inspection', file_name, 2))
                if result1 == 1:
                    print 'ok'
                if result2 == 1:
                    print 'ok'


if __name__ == '__main__':
    main()
