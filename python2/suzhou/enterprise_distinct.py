# -*- coding: utf-8 -*-
from mysql import query, query_one, save


def delelte(enterprise_id):
    try:
        save(sql=u'DELETE FROM `base_enterprise` WHERE `id` = %s', list1=(enterprise_id, ))
    except Exception as e:
        print e


def handle():
    enterprise_list = query(sql=u'''SELECT GROUP_CONCAT(`id`) 
                                            FROM `base_enterprise` 
                                            GROUP BY  `name`,  `code` 
                                            HAVING COUNT(*) > 1''')
    for enterprise in enterprise_list:
        print enterprise
        enterprise_ids = enterprise.get("GROUP_CONCAT(`id`)").split(",")
        flag = 0
        while flag < len(enterprise_ids):
            delelte(enterprise_ids[flag-1])
            flag += 1


def main():
    handle()

if __name__ == '__main__':
    main()
