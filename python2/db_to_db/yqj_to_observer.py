#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysql import query, query_one, save

db_connect_config = {
    'host':'192.168.1.205',
    'username':'shendu',
    'password':'P@55word',
    'database':'yqj',
    'port':13306
}

db_connect_config2 = {
    'host':'192.168.1.187',
    'username':'root',
    'password':'123456',
    'database':'observer',
    'port':3306
}

def event_article():
    event_article_count = query_one(sql=u'SELECT COUNT(*) FROM `topic_articles`', 
                                    host=db_connect_config.get('host'),
                                    username=db_connect_config.get('username'),
                                    password=db_connect_config.get('password'),
                                    database=db_connect_config.get('database'),
                                    port=db_connect_config.get('port')).get('COUNT(*)')
    
    index = 0
    while index < event_article_count:
        event_article_list = query(sql=u'SELECT * FROM `topic_articles` ORDER BY `id` DESC LIMIT %s, 100', 
                                list1=(index,),
                                host=db_connect_config.get('host'),
                                username=db_connect_config.get('username'),
                                password=db_connect_config.get('password'),
                                database=db_connect_config.get('database'),
                                port=db_connect_config.get('port'))
        index += 100

        for event_article in event_article_list:
            event_id = event_article.get('topic_id')
            article_id = event_article.get('article_id')

            event = query_one(sql=u'SELECT `area_id`, `source`, `keywords` FROM `topic`', 
                            host=db_connect_config.get('host'),
                            username=db_connect_config.get('username'),
                            password=db_connect_config.get('password'),
                            database=db_connect_config.get('database'),
                            port=db_connect_config.get('port'))
            area_id = event.get('area_id')
            event_source = event.get('source')
            event_keywords = event.get('keywords')

            yqj_area =  query_one(sql=u'SELECT `name`, `level` FROM `area` WHERE `id`=%s', 
                            list1=(area_id,),
                            host=db_connect_config.get('host'),
                            username=db_connect_config.get('username'),
                            password=db_connect_config.get('password'),
                            database=db_connect_config.get('database'),
                            port=db_connect_config.get('port'))

            observer_area = query_one(sql=u'SELECT `id` FROM `base_area` WHERE `name`=%s AND `level`=%s', 
                            list1=(yqj_area.get('name'),yqj_area.get('level'),),
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))

            article_category = query_one(sql=u'SELECT `id` FROM `base_articlecategory` WHERE `name`=%s AND `level`=%s', 
                            list1=(u'质量事件',1,),
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))

            save(sql=u'UPDATE `base_article` SET `source`=%s, `risk_keyword`=%s, `category_id`=%s, `area_id`=%s WHERE id=%s',
                            list1=(event_source, event_keywords, article_category.get('id'), observer_area.get('id'),article_id,), 
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))



def risk_article():
    risk_articles_count = query_one(sql=u'SELECT COUNT(*) FROM `risk_articles`', 
                                    host=db_connect_config.get('host'),
                                    username=db_connect_config.get('username'),
                                    password=db_connect_config.get('password'),
                                    database=db_connect_config.get('database'),
                                    port=db_connect_config.get('port')).get('COUNT(*)')
    
    index = 0
    while index < risk_articles_count:
        risk_articles_list = query(sql=u'SELECT * FROM `risk_articles` ORDER BY `id` DESC LIMIT %s, 100', 
                                list1=(index,),
                                host=db_connect_config.get('host'),
                                username=db_connect_config.get('username'),
                                password=db_connect_config.get('password'),
                                database=db_connect_config.get('database'),
                                port=db_connect_config.get('port'))
        index += 100

        for risk_articles in risk_articles_list:
            risk_id = risk_articles.get('risk_id')
            article_id = risk_articles.get('article_id')

            risk = query_one(sql=u'SELECT `area_id`, `source`, `keywords` FROM `topic`', 
                            host=db_connect_config.get('host'),
                            username=db_connect_config.get('username'),
                            password=db_connect_config.get('password'),
                            database=db_connect_config.get('database'),
                            port=db_connect_config.get('port'))
            area_id = risk.get('area_id')
            risk_source = risk.get('source')
            risk_keywords = event.get('keywords')
            risk_score = event.get('score')

            yqj_area =  query_one(sql=u'SELECT `name`, `level` FROM `area` WHERE `id`=%s', 
                            list1=(area_id,),
                            host=db_connect_config.get('host'),
                            username=db_connect_config.get('username'),
                            password=db_connect_config.get('password'),
                            database=db_connect_config.get('database'),
                            port=db_connect_config.get('port'))

            observer_area = query_one(sql=u'SELECT `id` FROM `base_area` WHERE `name`=%s AND `level`=%s', 
                            list1=(yqj_area.get('name'),yqj_area.get('level'),),
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))

            article_category = query_one(sql=u'SELECT `id` FROM `base_articlecategory` WHERE `name`=%s AND `level`=%s', 
                            list1=(u'风险快讯',1,),
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))

            save(sql=u'UPDATE `base_article` SET `source`=%s, `risk_keyword`=%s, `score`=%s, `category_id`=%s, `area_id`=%s WHERE `id`=%s',
                            list1=(risk_source, risk_keywords, risk_score, article_category.get('id'), observer_area.get('id'), article_id), 
                            host=db_connect_config2.get('host'),
                            username=db_connect_config2.get('username'),
                            password=db_connect_config2.get('password'),
                            database=db_connect_config2.get('database'),
                            port=db_connect_config2.get('port'))





def main():
    event_article()
    risk_article()

if __name__ == '__main__':
    main()