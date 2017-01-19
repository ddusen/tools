# -*- coding: utf-8 -*-
import sys
import xlrd
import xlwt

from datetime import date,datetime
from openpyxl.reader.excel import load_workbook as lw
from mysql import query, query_one, save

reload(sys)
sys.setdefaultencoding('utf8')

#读取 excel 表格, 通过读取的数据向数据库查询 level
def insert_data():

    # 打开文件
    workbook = xlrd.open_workbook(r'/home/dusen/Documents/changzhou_industry.xls')

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
    string = []

    def insert_data(column, industry_id, industry_name, string):
        if column == industry_name and column not in string:
            string.append(column)
            print colunm, industry_id, industry_name, string
            save(sql = "INSERT INTO riskmonitor_areaindustry(name,area_id, industry_id ) values(%s, %s, %s)", list1=(industry_name, 2360, industry_id))


    industry_data =  query(u"""SELECT id, name, level FROM industry""")
    count = 0

    for r in xrange(1,rownum):
        count += 1
        print '正在插入第 %s 条数据~~~' % count
        rowValue = sheet1.row_values(r)

        column1 = rowValue[0]
        column2 = rowValue[1]
        column3 = rowValue[2]
        column4 = rowValue[3]

        for i in industry_data:
            industry_id = i.get('id')
            industry_name = i.get('name')
            industry_level = i.get('level')

            if industry_level == 1:
                insert_data(column = column1, industry_id = industry_id, industry_name = industry_name, string = string)
            elif industry_level == 2:
                insert_data(column = column2, industry_id = industry_id, industry_name = industry_name, string = string)
            elif industry_level == 3:
                if column3.find(',') != -1:
                    for name in column3.split(','):
                        insert_data(column = name, industry_id = industry_id, industry_name = industry_name, string = string)
                else:
                    insert_data(column = column3, industry_id = industry_id, industry_name = industry_name, string = string)
            elif industry_level == 4:
                if column4.find(',') != -1:
                    for name in column4.split(','):
                        insert_data(column = name, industry_id = industry_id, industry_name = industry_name, string = string)
                else:
                    insert_data(column = column4, industry_id = industry_id, industry_name = industry_name, string = string)


    print '\n执行数据库添加操作成功! 本次共插入 %s 条数据' % count





if __name__ == '__main__':
    insert_data()


