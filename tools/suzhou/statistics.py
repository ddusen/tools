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

def insert_data():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/2015年全年苏州市市级监督抽查汇总表.xls'
    data_row = read_xls(xls_path)

    for index, item in enumerate(data_row):
        product = item[1]
        enterprise = item[5]
        is_qualified = 1 if item[8] == u'合格' else 0
        if product is not None and enterprise is not None:
            if save(sql=u"""INSERT INTO `statistics_resulttwo`(`product`, `enterprise`, `is_qualified`) VALUES(%s, %s, %s)""", list1=(product, enterprise, is_qualified)):
                print "INSERT <%s, %s, %s> SUCCESSFUL !" % (product, enterprise, is_qualified)

def statistics():
    xls_path = r'/home/sdu/MyProject/tools/tools/suzhou/2016年市抽数据.xls'
    data_row = read_xls(xls_path)

    two_consecutive_failed_list = []
    the_last_result_list = []
    follow_the_situation_list = []
    for index, item in enumerate(data_row):
        product = item[2]
        enterprise = item[6]
        is_qualified = 1 if item[9] == u'合格' else 0
        if index > 0 :
            query_data = query(sql=u"""SELECT `is_qualified` FROM `statistics_resulttwo` WHERE `product` = %s AND `enterprise` = %s""", list1=(product, enterprise))
            if query_data != ():
                two_consecutive_failed = u'否' if query_data[0].get('is_qualified') else u'否' if item[9] == u'合格' else u'是'
                the_last_result = u'合格' if query_data[0].get('is_qualified') else u'不合格'
                follow_the_situation = u'是' if the_last_result is not None else u'否'
            else:
                two_consecutive_failed = u'否'
                the_last_result = u''
                follow_the_situation = u'否'
            two_consecutive_failed_list.append(two_consecutive_failed)
            the_last_result_list.append(the_last_result)
            follow_the_situation_list.append(follow_the_situation)

    return (two_consecutive_failed_list, the_last_result_list, follow_the_situation_list)

def write_xls():
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet('sheet_1', cell_overwrite_ok=True)
    result = statistics()
    two_consecutive_failed_list = result[0]
    the_last_result_list = result[1]
    follow_the_situation_list = result[2]

    for index, item in enumerate(two_consecutive_failed_list):
        table.write(index, 0, item) # 行 列 值

    for index, item in enumerate(the_last_result_list):
        table.write(index, 1, item)
    
    for index, item in enumerate(follow_the_situation_list):
        table.write(index, 2, item)

    # 保存文件
    file.save('/home/sdu/MyProject/tools/tools/suzhou/statistics.xls')

def main():
    # insert_data()
    # statistics()
    write_xls()

if __name__ == '__main__':
    main()
