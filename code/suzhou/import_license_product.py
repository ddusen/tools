# -*- coding: utf-8 -*-
import xlrd
import xlwt
import uuid
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

def insert_data():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/苏州工业产品许可证分类目录.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        product = item[0]
        code = str(item[2]).split(".")[0]
        code = "-" if code == "" else code

        if product == "":
            continue
            
        if query(sql=u'SELECT COUNT(*) "count" FROM base_licenseproduct WHERE name = %s AND code = %s ', list1=(product, code))[0].get('count') == 0 :
            if save(sql=u'INSERT INTO base_licenseproduct(name, code, status) VALUES(%s, %s, 1)', list1=(product, code)):
                print "INSERT LICENSE PRODUCT < %s > SUCCESS !" % product

                
def main():
    insert_data()

if __name__ == '__main__':
    main()
