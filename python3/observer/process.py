import os, sys
sys.path.append(os.getcwd())

from configparser import (ConfigParser, RawConfigParser, )

from utils.db.mysql import (query, query_one, save, )


# 读取 config.ini 配置项
def read_config():
    cfg = ConfigParser()
    cfg.read('observer/config.ini')
    conf = {
        'mysql':{
            'host': cfg.get('mysql', 'host'),
            'port': int(cfg.getint('mysql', 'port')),
            'user': cfg.get('mysql', 'user'),
            'passwd': cfg.get('mysql', 'passwd'),
            'charset': cfg.get('mysql', 'charset'),
            'db': cfg.get('mysql', 'db'),
        },
        'sync':{
            'yqj.article': int(cfg.get('sync', 'yqj.article')),
            'yqj.inspection': int(cfg.get('sync', 'yqj.inspection')),
            'yqj2.risk_news': int(cfg.get('sync', 'yqj2.risk_news')),
            'yqj2.inspection': int(cfg.get('sync', 'yqj2.inspection')),
        }
    }
    return conf

# 写入 config.ini 配置项
def write_config(section, key, value):
    cfg = RawConfigParser()
    cfg.read('observer/config.ini')
    if section not in cfg.sections():
        cfg.add_section(section)

    cfg.set(section, key, value)

    with open('observer/config.ini', 'w') as f:
        cfg.write(f)

def yqj_article_total(mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT COUNT(*) FROM article'
    return query_one(sql=sql, db_config=mysql_conf)[0]

def yqj_articles(page, length, mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT `title`, `url`, `pubtime`, `area_id`, `publisher_id`, `id` FROM `article` ORDER BY `pubtime` DESC LIMIT %s, %s'
    return query(sql=sql, db_config=mysql_conf, list1=(page, length, ))

def yqj_area(area_id, mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT `name` FROM `area` WHERE `id` = %s'
    return query_one(sql=sql, db_config=mysql_conf, list1=(area_id, ))[0]

def yqj_publisher(publisher_id, mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT `publisher` FROM `articlepublisher` WHERE `id` = %s'
    return query_one(sql=sql, db_config=mysql_conf, list1=(publisher_id, ))[0]

def yqj_categories(article_id, mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT `category_id` FROM `category_articles` WHERE `article_id` = %s'
    return query(sql=sql, db_config=mysql_conf, list1=(article_id, ))

def yqj_categories_to_observer_categories(categories):
    c_dict = {
        1: '00031',
        2: '00032',
        3: '00033',
        4: '00040',
        5: '00034',
        6: '00035',
        7: '00036',
        8: '00037',
        9: '00038',
        10: '00039',
        11: '0003',
        13: '0001',
        15: '0002',
    }
    temp = []
    for c in categories:
        if c_dict.get(c):
           temp.append(c_dict[c])
    return temp

def observer_area(name, mysql_conf):
    mysql_conf['db'] = 'observer'
    sql = 'SELECT `id` FROM `base_area` WHERE `name` = %s LIMIT 0, 1'
    area_id = query_one(sql=sql, db_config=mysql_conf, list1=(name, ))

    if not area_id:
        area_id = query_one(sql=sql, db_config=mysql_conf, list1=("全国", ))

    return area_id

def observer_article_save(guid, title, url, pubtime, source, risk_keyword='', invalid_keyword='', status=1, mysql_conf={}):
    mysql_conf['db'] = 'observer'
    sql = 'SELECT COUNT(*) FROM `base_article` WHERE `guid` = %s'
    if not query_one(sql=sql, db_config=mysql_conf, list1=(guid, ))[0]:
        sql = '''INSERT INTO `base_article`(`guid`, `title`, `url`, `pubtime`, `source`, `score`, `risk_keyword`, `invalid_keyword`, `status`, `publisher`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        save(sql=sql, db_config=mysql_conf, list1=(guid, title, url, pubtime, source, 0, risk_keyword, invalid_keyword, status, '', ))

def observer_article_area_save(guid, area_id, mysql_conf):
    mysql_conf['db'] = 'observer'
    sql = 'SELECT COUNT(*) FROM `base_articlearea` WHERE `article_id` = %s AND `area_id` = %s'

    if not query_one(sql=sql, db_config=mysql_conf, list1=(guid, area_id, ))[0]:
        sql = 'INSERT INTO `base_articlearea`(`article_id`, `area_id`) VALUES (%s, %s)'
        save(sql=sql, db_config=mysql_conf, list1=(guid, area_id, ))

def observer_article_category_save(guid, category_id, mysql_conf):
    mysql_conf['db'] = 'observer'
    sql = 'SELECT COUNT(*) FROM `base_articlecategory` WHERE `article_id`=%s AND `category_id`=%s'

    if not query_one(sql=sql, db_config=mysql_conf, list1=(guid, category_id, ))[0]:
        sql = 'INSERT INTO `base_articlecategory`(`article_id`, `category_id`) VALUES (%s, %s)'
        save(sql=sql, db_config=mysql_conf, list1=(guid, category_id, ))

def yqj_inspection_total(mysql_conf):
    mysql_conf['db'] = 'yqj'
    sql = 'SELECT COUNT(*) FROM inspection'
    return query_one(sql=sql, db_config=mysql_conf)[0]

def yqj2_risknews_total(mysql_conf):
    mysql_conf['db'] = 'yqj2'
    sql = 'SELECT COUNT(*) FROM risk_news'
    return query_one(sql=sql, db_config=mysql_conf)[0]

def yqj2_risknews(page, length, mysql_conf):
    mysql_conf['db'] = 'yqj2'
    sql = 'SELECT `id`, `title`, `url`, `pubtime`, `area_id`, `publisher_id`, `is_delete`, `risk_keyword`, `invalid_keyword` FROM `risk_news` ORDER BY `pubtime` DESC LIMIT %s, %s'
    return query(sql=sql, db_config=mysql_conf, list1=(page, length, ))

def yqj2_area(area_id, mysql_conf):
    mysql_conf['db'] = 'yqj2'
    sql = 'SELECT `name` FROM `area` WHERE `id` = %s'
    return query_one(sql=sql, db_config=mysql_conf, list1=(area_id, ))[0]

def yqj2_publisher(publisher_id, mysql_conf):
    mysql_conf['db'] = 'yqj2'
    sql = 'SELECT `name` FROM `risk_news_publisher` WHERE `id` = %s'
    return query_one(sql=sql, db_config=mysql_conf, list1=(publisher_id, ))[0]
