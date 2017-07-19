# -*- coding: utf-8 -*-
from mysql import query, query_one, save

def main():
    group_by_name = query(sql=u'select name, count(*) from base_enterprise group by name')
    enterprise_name_list = []
    for data in group_by_name:
        if data.get('count(*)') > 1:
            enterprise_name_list.append(data.get("name"))

    for enterprise_name in enterprise_name_list:
        enterprises = query(sql=u'SELECT * FROM base_enterprise WHERE name = %s', list1=(enterprise_name,))
        enterprise_one = enterprises[0]
        enterprise_two = enterprises[1]

        enterprise_id = enterprise_two.get('id') if len(str(enterprise_one)) > len(str(enterprise_two)) else enterprise_two.get('id')

        if len(str(enterprise_one)) > len(str(enterprise_two)):
            print enterprise_one.get('id'), enterprise_two.get('id')

        print save(sql=u'DELETE FROM base_enterprise WHERE id = %s', list1=(enterprise_id,))

if __name__ == '__main__':
    main()
