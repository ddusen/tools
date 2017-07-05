# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date,datetime

from openpyxl.reader.excel import load_workbook as lw
import MySQLdb
import MySQLdb.cursors
import sys

reload(sys)
sys.setdefaultencoding('utf8')





'''
============================================> 分割线 <===============================================
=======================================> 以下是数据库操作代码 <=========================================
'''
class MySQL():
    def __init__(self, type='', cursorclass=MySQLdb.cursors.DictCursor):
        self.type = type
        self.cursorclass = cursorclass

    def open(self):
        # return MySQLdb.connect(
        #         '192.168.1.205',
        #         'shendu',
        #         'P@55word',
        #         'yqj2',
        #         charset='utf8',
        #         port=13306,
        #         cursorclass=self.cursorclass)
        return MySQLdb.connect(
                '192.168.1.185',
                'root',
                '123456',
                'yqj2',
                charset='utf8',
                port=3306,
                cursorclass=self.cursorclass)
        # return MySQLdb.connect(
        #     '127.0.0.1',
        #     'root',
        #     '123456',
        #     'python',
        #     charset='utf8',
        #     port=3306,
        #     cursorclass = self.cursorclass
        #     )

def query(sql,list1=()):
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql,list1)
    result = cursor.fetchall()

    db.commit()
    db.close()
    return result

def query_one(sql,list1=()):
    # if not list1:
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchone()

    db.commit()
    db.close()
    return result


def save(sql,list1=()):
    db = MySQL().open()
    cursor = db.cursor()
    try:
        result = cursor.execute(sql,list1)
        db.commit()
        return result
    except Exception ,e:
        print e
        print 'mysql save fail'
        db.rollback()
        return None
    db.close()





''' SQL 语句 '''
select_sql = u"""SELECT id FROM industry WHERE name = %s"""
insert_sql = u"""INSERT INTO industry(name,level,parent_id) VALUES(%s, %s, %s)"""

# select_sql = u"""SELECT id FROM users WHERE username = %s"""
# insert_sql = u"""INSERT INTO users(username,password) VALUES(%s, %s)"""



'''
============================================> 分割线 <===============================================
=======================================> 以下是Excel操作代码 <=========================================
'''



#读取 excel 表格, 通过读取的数据向数据库查询 level
def insert_data():

    # 打开文件
    workbook = xlrd.open_workbook(r'/home/dusen/Documents/2016.08.01/industry.xls')

    # 获取所有sheet
    # print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[0]

    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('sheet2')

    sheetName = sheet1.name; # sheet 的名称
    rownum = sheet1.nrows; # 行数
    colnum = sheet1.ncols; # 列数
    colnames = sheet1.row_values(0)

    print 'sheetName = %s , rownum = %s, colnum = %s' % (sheetName, rownum, colnum)

    industry_name_1 = ''
    ids_1 = ''
    industry_name_2 = ''
    ids_2 = ''

    industry_name_3 = ''
    ids_3 = ''

    count = 0
    for r in xrange(1,rownum):
        count += 1
        print '正在插入第 %s 条数据~~~' % count
        rowValue = sheet1.row_values(r)

        column1 = rowValue[0]
        column2 = rowValue[1]
        column3 = rowValue[2]
        column4 = rowValue[3]

        if column1 != 'A':
            industry_name_1 = column1
            result = save(sql = insert_sql, list1 =(industry_name_1,1,None))
            ids_1 = query_one(sql = select_sql,list1 = (industry_name_1))
            ids_1 = ids_1['id']

            if column2 != 'A':
                industry_name_2 = column2
                result = save(sql = insert_sql, list1 =(industry_name_2,2,ids_1))
                ids_2 = query_one(sql = select_sql,list1 = (industry_name_2))
                ids_2 = ids_2['id']

                if column3 != 'A':
                    industry_name_3 = column3
                    result = save(sql = insert_sql, list1 =(column3,3,ids_2))
                    ids_3 = query_one(sql = select_sql,list1 = (industry_name_3))
                    ids_3 = ids_3['id']

                    if column4 != 'A':
                        column4_str = column4.split(',')
                        for s in column4_str:
                            count += 1
                            result = save(sql = insert_sql, list1 =(s,4,ids_3))

        else:
            if column2 != 'A':
                industry_name_2 = column2
                result = save(sql = insert_sql, list1 =(industry_name_2,2,ids_1))
                ids_2 = query_one(sql = select_sql,list1 = (industry_name_2))
                ids_2 = ids_2['id']

                if column3 != 'A':
                    industry_name_3 = column3
                    result = save(sql = insert_sql, list1 =(column3,3,ids_2))
                    ids_3 = query_one(sql = select_sql,list1 = (industry_name_3))
                    ids_3 = ids_3['id']

                    if column4 != 'A':
                        column4_str = column4.split(',')
                        for s in column4_str:
                            count += 1
                            result = save(sql = insert_sql, list1 =(s,4,ids_3))
            else:
                if column3 != 'A':
                    industry_name_3 = column3
                    result = save(sql = insert_sql, list1 =(column3,3,ids_2))
                    ids_3 = query_one(sql = select_sql,list1 = (industry_name_3))
                    ids_3 = ids_3['id']

                    if column4 != 'A':
                        column4_str = column4.split(',')
                        for s in column4_str:
                            count += 1
                            result = save(sql = insert_sql, list1 =(s,4,ids_3))
                else:
                    if column4 != 'A':
                        column4_str = column4.split(',')
                        for s in column4_str:
                            count += 1
                            result = save(sql = insert_sql, list1 =(s,4,ids_3))



    print '\n执行数据库添加操作成功! 本次共插入 %s 条数据' % count





if __name__ == '__main__':
    insert_data()


