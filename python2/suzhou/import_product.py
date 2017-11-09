# -*- coding: utf-8 -*-
import re
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
    for i in xrange(0, rownum):
        data_row.append(sheet1.row_values(i))

    return data_row


def insert_data():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/product_code.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        level_one = item[0]
        level_two = item[1]
        level_three = item[2]
        level_four = item[3]


        if level_one == "":
            continue

        level_one_obj = query(sql=u'SELECT * FROM base_product WHERE level=1 AND name=%s', list1=(re.findall(r'(.*?)\(.*?\)', level_one)[0],))
        if level_one_obj == ():
            name = re.findall(r'(.*?)\(.*?\)', level_one)[0]
            if name == "":
                continue

            code = re.findall(r'.*?\((.*?)\)', level_one)[0]
            if save(sql=u'INSERT INTO base_product(name, code, level, status) VALUES(%s, %s, 1, 1)', list1=(name, code, )):
                print "INSERT < %s > CODE{ %s } SUCCESS!" % (name, code)
        else:
            if level_two == "":
                continue

            level_two_obj = query(sql=u'SELECT * FROM base_product WHERE level=2 AND name=%s', list1=(re.findall(r'(.*?)\(.*?\)', level_two)[0],))
            if level_two_obj == ():
                name = re.findall(r'(.*?)\(.*?\)', level_two)[0]
                if name == "":
                    continue

                code = re.findall(r'.*?\((.*?)\)', level_two)[0]
                parent_id = level_one_obj[0].get('id')
                if save(sql=u'INSERT INTO base_product(name, code, level, status, parent_id) VALUES(%s, %s, 2, 1, %s)', list1=(name, code, parent_id, )):
                    print "INSERT < %s > CODE{ %s } SUCCESS!" % (name, code)
            else:
                if level_three == "":
                    continue

                level_three_obj = query(sql=u'SELECT * FROM base_product WHERE level=3 AND name=%s', list1=(re.findall(r'(.*?)\(.*?\)', level_three)[0],))
                if level_three_obj == ():
                    name = re.findall(r'(.*?)\(.*?\)', level_three)[0]
                    if name == "":
                        continue

                    code = re.findall(r'.*?\((.*?)\)', level_three)[0]
                    parent_id = level_two_obj[0].get('id')
                    if save(sql=u'INSERT INTO base_product(name, code, level, status, parent_id) VALUES(%s, %s, 3, 1, %s)', list1=(name, code, parent_id, )):
                        print "INSERT < %s > CODE{ %s } SUCCESS!" % (name, code)
                else:
                    if level_four == "":
                        continue

                    level_four_obj = query(sql=u'SELECT * FROM base_product WHERE level=4 AND name=%s', list1=(re.findall(r'(.*?)\(.*?\)', level_four)[0],))
                    if level_four_obj == ():
                        name = re.findall(r'(.*?)\(.*?\)', level_four)[0]
                        if name == "":
                            continue

                        code = re.findall(r'.*?\((.*?)\)', level_four)[0]
                        parent_id = level_three_obj[0].get('id')
                        if save(sql=u'INSERT INTO base_product(name, code, level, status, parent_id) VALUES(%s, %s, 4, 1, %s)', list1=(name, code, parent_id, )):
                            print "INSERT < %s > CODE{ %s } SUCCESS!" % (name, code)
                
def main():
    insert_data()

if __name__ == '__main__':
    main()
