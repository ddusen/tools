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
        return MySQLdb.connect(
                '192.168.1.205',
                'shendu',
                'P@55word',
                'yqj2',
                charset='utf8',
                port=13306,
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

def query(sql,list1=[]):
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql,list1)
    result = cursor.fetchall()

    db.commit()
    db.close()
    return result

def query_one(sql,list1=[]):
    # if not list1:
    db = MySQL().open()
    cursor = db.cursor()
    cursor.execute(sql, list1)
    result = cursor.fetchone()

    db.commit()
    db.close()
    return result
    # else:
    #     db = MySQL('conf').open()
    #     cursor = db.cursor()
    #     sql = u"""SELECT level FROM industry WHERE name = %(name)s"""
    #     cursor.execute(sql,{'name':'日常消耗品'})
    #     result = cursor.fetchone()

    #     db.commit()
    #     db.close()
    #     return result

def save(sql,list1=[]):
    db = MySQL().open()
    cursor = db.cursor()
    try:
        result = cursor.execute(sql, list1)

        db.commit()
        return result
    except Exception ,e:
        print e
        print 'mysql save fail'
        db.rollback()
        return None
    db.close()




''' SQL 语句 '''
select_sql = u"""SELECT level FROM industry WHERE name = %s"""
insert_sql = u"""INSERT INTO user_industry(name,industry_id,user_id) VALUES(%s, %s, %s)"""

# select_sql = u"""SELECT id FROM users WHERE username = %s"""
# insert_sql = u"""INSERT INTO users(username,password) VALUES(%s, %s)"""



'''
============================================> 分割线 <===============================================
=======================================> 以下是Excel操作代码 <=========================================
'''





#读取 excel 表格, 通过读取的数据向数据库查询 level
def getLevelByReadExcel():

    # 打开文件
    workbook = xlrd.open_workbook(r'/home/dusen/Documents/name01.xls')

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


    # 获取整行和整列的值（数组）
    list2 = []
    for r in range(1, rownum):
        rowValue = sheet1.row_values(r)
        for index in rowValue:
            # level = {'id':1}
            # if index != None:
            #     level = query_one(sql = select_sql,list1=[index])
            print index

            list2.append(level)
    return list2

def insertDataByReadExcel(list1):
    wb = lw(filename = '/home/dusen/Documents/data01.xlsx')
    ws = wb.get_sheet_by_name(wb.get_sheet_names()[0])    # <worksheet "data">

    rows = ws.get_highest_row()         # 最大行数
    columns = ws.get_highest_column()   # 最大列数

    data = []
    count = 0
    for rx in range(2, rows+1):
        for cx in range(1, columns+1):
            data.append(str(ws.cell(row=rx, column=cx).value))
        
        try:
            ids = list1[count]['level']
        except:
            ids = 1
        # result = save(sql = insert_sql, list1 = [data[0], int(ids), int(data[2])])
        
        count += 1
        print '正在插入第 %d 条数据~~~' % count
        data = []
    return count



if __name__ == '__main__':

    # '''测试'''
    # result = query("SELECT * FROM users ")
    # print result
    # print save(sql = u'''INSERT INTO user_industry(name,industry_id,user_id) VALUES(%s, %s, %s)''',list1=['测试',1,9])

    all_level = getLevelByReadExcel()
    # print all_level

    result = insertDataByReadExcel(all_level)
    print '执行数据库添加操作成功! 本次共插入 %s 条数据' % result
    















