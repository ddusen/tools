# -*- coding: utf-8 -*-
import sys
import xlrd
import xlwt
import pickle
import jieba.analyse as ja

from datetime import date, datetime
from openpyxl.reader.excel import load_workbook as lw
from collections import Counter


def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'/home/sdu/Documents/traveldata.xls')
    # 获取所有sheet
    # print workbook.sheet_names() # [u'sheet1', u'sheet2']
    sheet1_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    # sheet2 = workbook.sheet_by_name('sheet2')
    sheetName = sheet1.name  # sheet 的名称
    rownum = sheet1.nrows  # 行数
    colnum = sheet1.ncols  # 列数
    colnames = sheet1.row_values(0)

    print ('sheetName = %s , rownum = %s, colnum = %s' % (sheetName, rownum, colnum))

    all_data = []
    for r in xrange(1, rownum):
        rowValue = sheet1.row_values(r)
        all_data.append(rowValue)

    return all_data


def second_analysis():
    all_data = read_excel()
    d_1 = []


    for each in all_data:
        d_1.append(each[0])
        d_1.append(each[1])
        d_1.append(each[2])

    string = []
    data = {}
    for each_1 in d_1:
        for each_2 in all_data:
            if each_2[0] == each_1:
                string.append(each_2[1])
        # str = '\n' + '--' * 50 + '\n'
        data[each_1] = ''.join(string)
        string = []

    return data


def main():

    data = second_analysis()

    ALL_DATA  = ""

    for k, v in data.items():
        ALL_DATA = "'" + k + ':' + v + "', "
    

    ALL_DATA = Counter(ja.extract_tags(ALL_DATA, topK=50000, withWeight=True, allowPOS=()))

    for i in ALL_DATA:
        print i 


if __name__ == '__main__':
    main()
