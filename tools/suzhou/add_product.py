# -*- coding: utf-8 -*-
from mysql import query, query_one, save
from mysql_2 import query_2, query_one_2, save_2


def get_yqj2_industry():
    return query_2(sql=u"SELECT `name` FROM `industry` WHERE level = 3")


def add_product():

    product_category_list = [u"日用消费品", u"建筑装饰装修材料", u"工业生产资料", u"农业生产资料", u"食品相关产品"]
    for product_category in product_category_list:
        if save(sql=u"INSERT INTO `base_product_category`()")


    industry_dict = get_yqj2_industry()

    for k, v in industry_dict.items():
        if save(sql=u"INSERT INTO `base_product`(`name`, `specifications`, `date`, `category_id`, `origin_id`) VALUES(%s,'XL',now(),%s,%s)", list1=(v, ))==1:
            print "insert product <%s , %s> successful !" % (k, v)
