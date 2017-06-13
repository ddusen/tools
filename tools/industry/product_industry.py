# -*- coding: utf-8 -*-
from mysql import query, query_one, save
from mysql2 import query as query2, query_one as query_one2, save as save2


def data_changes():
    for level in xrange(1,5):
        products = query2(sql=u"SELECT `code`, `name` FROM `base_product` WHERE `level`=%s", list1=(level, ))
        for product in products:
            code = product.get('code')
            name = product.get('name')
            if not save(sql=u"UPDATE `industry` SET `code`=%s WHERE `level`=%s AND `name`=%s", list1=(code, level, name, )):
                print code, name, level

def insert():
    industries = query(sql=u"SELECT id, name FROM industry")
    for industry in industries:
        print save(sql=u'INSERT INTO riskmonitor_areaindustry(name, area_id, industry_id, status) VALUES(%s, 2368,  %s, 0)', list1=(industry.get('name'), industry.get('id')))

def hint_license():
    license_product = query2(sql=u"SELECT name FROM base_licenseproduct")
    for name in license_product:
        print save(sql=u"UPDATE riskmonitor_areaindustry SET status='4' WHERE name = %s AND area_id=2368", list1=(name.get('name'), ))

def main():
    hint_license()

if __name__ == '__main__':
    main()
