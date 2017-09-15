# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors

db_connect_config = {
    'host':'127.0.0.1',
    'username':'root',
    'password':'123456',
    'database':'observer',
    'port':3306
}

class MySQL():

    def __init__(self, type='', cursorclass=MySQLdb.cursors.DictCursor):
        self.type = type
        self.cursorclass = cursorclass

    def open(self, host, username, password, database, port):
        return MySQLdb.connect(
                host,
                username,
                password,
                database,
                charset='utf8',
                port=port,
                cursorclass=self.cursorclass)


def query(sql, list1=(), host=db_connect_config.get('host'), username=db_connect_config.get('username'), password=db_connect_config.get('password'), database=db_connect_config.get('database'), port=db_connect_config.get('port')):
    db = MySQL().open(host=host,username=username,password=password,database=database,port=port)
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchall()

    db.commit()
    db.close()
    return result


def query_one(sql, list1=(), host=db_connect_config.get('host'), username=db_connect_config.get('username'), password=db_connect_config.get('password'), database=db_connect_config.get('database'), port=db_connect_config.get('port')):
    db = MySQL().open(host=host,username=username,password=password,database=database,port=port)
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchone()

    db.commit()
    db.close()
    return result


def save(sql, list1=(), host=db_connect_config.get('host'), username=db_connect_config.get('username'), password=db_connect_config.get('password'), database=db_connect_config.get('database'), port=db_connect_config.get('port')):
    db = MySQL().open(host=host,username=username,password=password,database=database,port=port)
    cursor = db.cursor()
    try:
        result = cursor.execute(sql, list1)
        db.commit()
        return result
    except Exception, e:
        print e
        db.rollback()
        return None
    db.close()
