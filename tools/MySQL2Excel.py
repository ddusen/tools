#!/usr/bin/env python
#coding=utf-8

import sys
import MySQLdb
import xlwt

db=raw_input('请输入数据库名:')
table=raw_input('请输入数据表名:')


def xls(sql='select * from %s.%s'):
    #xls info
    wbk=xlwt.Workbook()
    sheet=wbk.add_sheet('sheet 1')
    #connect Info
    try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='123456')
        cursor=conn.cursor()
        cursor.execute('use information_schema')
        cursor.execute('select COLUMN_NAME  from COLUMNS where TABLE_NAME=%s and TABLE_SCHEMA=%s',(table,db))
        columnName=cursor.fetchall()
        columnLen=len(columnName)
        columnNum=0
        for data in range(columnLen):
                sheet.write(0,columnNum,columnName[columnNum][0])
                columnNum +=1
        cursor.execute(sql % (db,table))
        dataInfo=cursor.fetchall()
        rowLine=0
        for line in range(len(dataInfo)):
                lineInfo=dataInfo[line]
                rowLine+=1
                columnLine=0
                for row in lineInfo:
                        sheet.write(rowLine,columnLine,row)
                        columnLine+=1
        wbk.save('%s.xls' % table)
        cusor.close()
        conn.commit()
        conn.close()
    finally :
        conn.close()
        sys.exit(1)
if __name__=='__main__':
        xls()