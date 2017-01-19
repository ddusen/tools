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
    workbook = xlrd.open_workbook(r'/home/sdu/Documents/data.xls')
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


def first_analysis():
    data = pickle.load(open("data.pkl", "r"))
    data = data.split("\n")

    data_count = Counter(data)
    print ("从 事件性质 角度来看: ")
    print ("==" * 50)
    for k, v in data_count.iteritems():
        print '(', k, ')事件出现(', v, ')次.'

    print ("==" * 50)


def second_analysis():
    all_data = read_excel()
    d_1 = []
    d_2 = []
    d_3 = []

    for each in all_data:
        d_1.append(each[0])
        d_2.append(each[1])
        d_3.append(each[2])

    d_1_set = list(set(d_1))

    string = []
    data = {}
    for each_1 in d_1_set:
        for each_2 in all_data:
            if each_2[0] == each_1:
                string.append(each_2[1])
        # str = '\n' + '--' * 50 + '\n'
        data[each_1] = ''.join(string)
        string = []

    return data


def third_analysis():
    all_data = read_excel()
    d_1 = []
    d_2 = []
    d_3 = []

    for each in all_data:
        d_1.append(each[0])
        d_2.append(each[1])
        d_3.append(each[2])

    d_1_set = list(set(d_1))

    string = []
    data = {}
    for each_1 in d_1_set:
        for each_2 in all_data:
            if each_2[0] == each_1:
                string.append(each_2[2])
        # str = '\n' + '--' * 50 + '\n'
        data[each_1] = ''.join(string)
        string = []

    return data


def main():
    first_analysis()
    print('\n')


    print('\n')
    print'从 事件描述 角度来看: >>>'
    data = second_analysis()
    for k, v in data.items():
        print '关于', k, '的事件描述的高频词语如下:'
        string = "'" + k + ':' + v + "', "
        for i in ja.extract_tags(string, withWeight=False, allowPOS=()):
            print(i)


    print('\n')
    print'从 解决方案 角度来看: >>>'
    data = third_analysis()
    for k, v in data.items():
        print '关于', k, '的解决方案的高频词语如下:'
        string = "'" + k + ':' + v + "', "
        for i in ja.extract_tags(string, withWeight=False, allowPOS=()):
            print(i)



if __name__ == '__main__':
    main()
