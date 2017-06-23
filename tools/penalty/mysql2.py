# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors


class MySQL():

    def __init__(self, type='', cursorclass=MySQLdb.cursors.DictCursor):
        self.type = type
        self.cursorclass = cursorclass

    def open(self):
        return MySQLdb.connect(
                'localhost',
                'root',
                '123456',
                'postprocess',
                charset='utf8',
                port=3306,
                cursorclass=self.cursorclass)
        # return MySQLdb.connect(
        #     '127.0.0.1',
        #     'root',
        #     '123456',
        #     'test',
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
        db.rollback()
        return None
    db.close()
