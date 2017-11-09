# -*- coding: utf-8 -*-
import MySQLdb
import MySQLdb.cursors

from django.conf import settings


class mysql():
    def __init__(self, type='', cursorclass=MySQLdb.cursors.DictCursor):
        self.type = type
        self.cursorclass=cursorclass

    def open(self):
        # if not self.type:
        #     mysql_conn = settings.MYSQL_CONN_STR_DEFAULT
        #     return MySQLdb.connect(
        #         mysql_conn['host'],
        #         mysql_conn['username'],
        #         mysql_conn['password'],
        #         mysql_conn['name'],
        #         charset='utf8')
        # else:
        return MySQLdb.connect(
                    '192.168.1.205',
                    'shendu',
                    'P@55word',
                    'crawler',
                    charset='utf8',
                    port=13306,
                    cursorclass=self.cursorclass)


def query(sql, llist=[]):
    db = mysql().open()
    cursor = db.cursor()
    cursor.execute(sql, llist)
    result = cursor.fetchall()

    db.commit()
    db.close()
    return result


# return []
def query_one(sql='', llist=[], user=''):
    if not user:
        db = mysql().open()
        cursor = db.cursor()
        cursor.execute(sql, llist)
        result = cursor.fetchone()[0]

        db.commit()
        db.clone()
        return result
    else:
        db = mysql('conf').open()
        cursor = db.cursor()
        sql = u"""SELECT * FROM settings_one WHERE user_id=(SELECT id FROM auth_user WHERE
            username=%s)"""
        cursor.execute(sql, [user])
        result = cursor.fetchone()

        db.commit()
        db.close()
        return result


# return row (int)number
def save(sql, llist=[]):
    db = mysql().open()
    cursor = db.cursor()
    try:
        result = cursor.execute(sql, llist)
        db.commit()
        return result
    except:
        print "mysql save fail"
        db.rollback()
        return None
    db.close()


# if __name__ == '__main__':
    # sql = "insert into demo value(null,%s,%s)"
    # print sql
    # query()
    # n = save(sql,["xin1","pwd1"])
    # print n
    # sql = "select * from demo where pwd = %s"
    # l = query_one(sql,["pwd1"])
    # if l:
    #     print l[0],l[1],l[2]
        # for x in range(len(l)):
        #     print l[x][0],l[x][1],l[x][2]
    # else:
    #     print l
