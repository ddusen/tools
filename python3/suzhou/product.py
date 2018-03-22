#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from utils.db.mysql import query, query_one, save

def db_config():
    return {
        'host':'127.0.0.1',
        'port':3306,
        'user':'root',
        'passwd':'123456',
        'db':'postprocess'
    }


def insert():
    products = ['蓄电池',
                '实木地板',
                '实木复合地板',
                '浸渍纸层压木质地板',
                '干混砂浆',
                '家用空气净化器',
                '乘用车空气净化器',
                '铝合金建筑型材',
                '保险箱',
                '塑料管材',
                '食品相关',
                '化学纤维',
                '纺织面料',
                '低压电器',
                '电线电缆',
                '安全玻璃',
                '衬衫',
                '床上用品',
                '丝绸制品',
                '高效空气过滤器',
                '空气过滤器',
                '休闲服装',
                '校服',
                '双面呢大衣',
                '羽绒服',]
    for product in products:
        queryset = query(sql='''SELECT `name`, `code`, `level` FROM `base_samplingproduct` WHERE `name` = %s ''', 
                        list1=(product, ), 
                        db_config=db_config())
        if queryset:
            print('name: %s, code: %s, level: %s' % ())


if __name__ == '__main__':
    insert()
