# -*- coding: utf-8 -*-
from mysql import query, query_one, save


def delelte(publisher_id):
    try:
        save(sql=u'DELETE FROM `origin_inspection_publisher` WHERE `id` = %s', list1=(publisher_id, ))
    except Exception as e:
        print e


def handle():
    publisher_list = query(sql=u'''SELECT GROUP_CONCAT(`id`) 
                                            FROM `origin_inspection_publisher` 
                                            GROUP BY  `name` 
                                            HAVING COUNT(*) > 1''')
    for publisher in publisher_list:
        print publisher
        publisher_ids = publisher.get("GROUP_CONCAT(`id`)").split(",")
        flag = 0
        while flag < len(publisher_ids):
            delelte(publisher_ids[flag-1])
            flag += 1


def main():
    handle()

if __name__ == '__main__':
    main()
