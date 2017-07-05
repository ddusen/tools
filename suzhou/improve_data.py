# -*- coding: utf-8 -*-
import xlrd
import xlwt
from datetime import date, datetime

from openpyxl.reader.excel import load_workbook as lw
from mysql import query, query_one, save

def read_xls(xls_path):
    workbook = xlrd.open_workbook(xls_path)

    # get sheel
    sheet1_name = workbook.sheet_names()[0]

    # accoding to sheel get sheel content
    sheet1 = workbook.sheet_by_index(0)  # sheet index begin 0

    sheetName = sheet1.name  # sheet's name
    rownum = sheet1.nrows  # row number
    colnum = sheet1.ncols  # col number
    colnames = sheet1.row_values(0)

    print 'sheetName = %s , rownum = %s, colnum = %s' % (sheetName, rownum, colnum)

    data_row = []
    for i in xrange(1, rownum):
        data_row.append(sheet1.row_values(i))

    return data_row

def improve_one():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/苏州电线电缆许可证汇总168批.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if item[5] == u'':
            enterprise = item[1]
            if save(sql=u'''UPDATE base_enterprise SET is_not_license = 0 WHERE name = %s ''', list1=(enterprise, )):
                print "UPDATE < %s > SUCCESSFUL!" % enterprise

def improve_two():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/许可证信息.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        if item[1] != u'':
            enterprise = item[0]
            organization_code = item[1]
            if save(sql=u'''UPDATE base_enterprise SET organization_code = %s WHERE name = %s ''', list1=(organization_code, enterprise)):
                print "UPDATE < %s > SUCCESSFUL!" % enterprise

def main():
    improve_one()
    improve_two()

if __name__ == '__main__':
    main()
