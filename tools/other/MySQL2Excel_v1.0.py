#!/usr/bin/env python
# coding=utf-8

import sys
import MySQLdb
import xlwt
import mysql


reload(sys)
sys.setdefaultencoding('utf8')

db = raw_input('请输入数据库名:')
table = raw_input('请输入数据表名:')


def xls(sql='select * from %s.%s'):
    # xls info
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet 1')
    # connect Info
    try:
        conn = MySQLdb.connect(
            host='192.168.1.205', port=13306, charset='utf8', user='shendu', passwd='P@55word')
        cursor = conn.cursor()
        cursor.execute('use information_schema')
        cursor.execute(
            'select COLUMN_NAME  from COLUMNS where TABLE_NAME=%s and TABLE_SCHEMA=%s and ', (table, db))
        columnName = cursor.fetchall()
        columnLen = len(columnName)
        columnNum = 0
        for data in range(columnLen):
            sheet.write(0, columnNum, columnName[columnNum][0])
            columnNum += 1
        cursor.execute(sql % (db, table))
        dataInfo = cursor.fetchall()
        rowLine = 0
        dataInfo_len = len(dataInfo)
        for line in range(dataInfo_len):
            print '此次操作共需向 Excel 写入 %s 行数据, 现已写入 %s 行~~~' % (dataInfo_len, line+1)
            lineInfo = dataInfo[line]
            rowLine += 1
            columnLine = 0
            for row in lineInfo:
                sheet.write(rowLine, columnLine, row)
                columnLine += 1
        wbk.save('%s.xls' % table)
        cusor.close()
        conn.commit()
        conn.close()
    finally:
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    xls()
    print '操作成功~~~'
