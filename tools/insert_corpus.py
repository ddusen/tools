#!/usr/bin/python
# coding=utf-8
import MySQLdb
import MySQLdb.cursors
import sys
root_mod = '/home/dusen/shendu/api/api'
sys.path.append(root_mod)
import uuid
from datetime import datetime, timedelta
import os
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "observer.settings.development")

from observer.apps.corpus import admin

from observer.apps.corpus.models import Corpus
from observer.utils.crawler.api import CrawlerTask
from django_extensions.admin import ForeignKeyAutocompleteAdmin


# insert_crawler_sql = u"""INSERT  INTO
# `crawler_task`(`app`,`module`,`crawlerimpl`,`rank`,`url`,`data`,`priority`,`interval`,`timeout`,`create_at`,`update_at`,`last_run`,`next_run`,`status`)
# VALUES
# ('inspection','',%s,1,%s,%s,3,3600,3600,NOW(),NOW(),NOW(),NOW(),1);"""

corpus_words = u"""不合格 不达标 超标 褪色 致癌 危险 异味 PH值 纤维含量 过期 异物 色素 防腐剂 产品质量 抽查 整改 投诉 违规 风险 不安全 甲醛含量 伪冒 劣质 三无 污染 造假 噪音 故障 频发 事故 危机 曝光 预警 召回 爆炸 漏水 燃爆 伤害 自燃"""

insert_corpus_sql = u"""INSERT INTO corpus(uuid,riskword,invalidword,industry_id)values(%s,%s,'',%s)"""


class MySQL():

    def __init__(self, type='', cursorclass=MySQLdb.cursors.DictCursor):
        self.type = type
        self.cursorclass = cursorclass

    def open(self):
        return MySQLdb.connect(
            '192.168.1.205',
            'shendu',
            'P@55word',
            'yqj2',
            charset='utf8',
            port=13306,
            cursorclass=self.cursorclass)
       # return MySQLdb.connect(
       #          '192.168.1.205',
       #          'shendu',
       #          'P@55word',
       #          'yqj2',
       #          charset='utf8',
       #          port=13306,
       #          cursorclass=self.cursorclass)
        # return MySQLdb.connect(
        #         '192.168.1.185',
        #         'root',
        #         '123456',
        #         'yqj2',
        #         charset='utf8',
        #         port=3306,
        #         cursorclass=self.cursorclass)
        # return MySQLdb.connect(
        #     '127.0.0.1',
        #     'root',
        #     '123456',
        #     'python',
        #     charset='utf8',
        #     port=3306,
        #     cursorclass = self.cursorclass
        #     )


def query(sql, list1=()):
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchall()

    db.commit()
    db.close()
    return result


def query_one(sql, list1=()):
    # if not list1:
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchone()

    db.commit()
    db.close()
    return result


def save(sql, list1=()):
    db = MySQL().open()
    cursor = db.cursor()
    try:
        result = cursor.execute(sql, list1)
        db.commit()
        return result
    except Exception, e:
        print e
        print 'mysql save fail'
        db.rollback()
        return None
    db.close()


def get_industry_data():
    select_sql = u'''SELECT id,name FROM industry '''

    industry_data = query(sql=select_sql)

    # file = open('industry_data.pkl','wb')
    # pickle.dump(industry_data,file)
    # file.close()
    return industry_data


def exceute_sql(data):
    data_len = len(data)

    for index in xrange(data_len):
        # print
        # data[index]['uuid_data'],data[index]['industry_name'],data[index]['corpus_words'],''
        CrawlerTask(data[index]['uuid_data'], data[index][
                    'industry_name'], data[index]['corpus_words'], '').build()
        save(sql=insert_corpus_sql, list1=(
            data[index]['uuid_data'], corpus_words, int(data[index]['industry_id'])))
        print index


def run():
    industry_data = get_industry_data()

    all_data = []
    for each in industry_data:
        data = {}

        data['industry_id'] = int(each['id'])
        data['industry_name'] = each['name']

        data['uuid_data'] = uuid.uuid1()
        data['corpus_words'] = list(set(corpus_words.split()))
        data['source_type'] = u'行业监测'

        all_data.append(data)
        
    exceute_sql(data=all_data)
