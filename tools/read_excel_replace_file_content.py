# -*- coding: utf-8 -*-
import xlrd
import xlwt
import os
from openpyxl.reader.excel import load_workbook as lw
import sys

reload(sys)
sys.setdefaultencoding('utf8')


def replace_str(file_content, filename, old_str='', new_str=''):

    old_str_count = file_content.count(old_str)

    if old_str_count > 0:
        print '文件 %s 中共有 %s 个 [%s]' % (filename, old_str_count, old_str)
        print '您确定要把 [%s] 替换为 [%s] 吗?' % (old_str, new_str)

        operate = raw_input('[YES/NO]:')

        if operate in ['YES', 'yes', '']:
            new_file = file_content.replace(old_str, new_str)
            return new_file
        else:
            return ''
    else:
        return ''


def rw_file(filename, old_str, new_str):
    try:
        file = open(filename, 'r')
        file.seek(0, 0)
        file_content = file.read()

        new_file = replace_str(file_content, filename, old_str, new_str)

        if new_file != '':
            file = open(filename, 'w')
            file.seek(0, 0)
            file.write(new_file)
            print """
                             ./+o+-
                     yyyyy- -yyyyyy+
                  ://+//////-yyyyyyo
              .++ .:/++++++/-.+sss/`
            .:++o:  /++++++++/:--:/-
           o:+o+:++.`..```.-/oo+++++/
          .:+o:+o/.          `+sssoo+/
     .++/+:+oo+o:`             /sssooo.
    /+++//+:`oo+o      ok       /::--:.
    \+/+o+++`o++o               ++////.
     .++.o+++oo+:`             /dddhhh.
          .+.o+oo:.          `oddhhhh+
           \+.++o+o``-````.:ohdhhhhh+
            `:o+++ `ohhhhhhhhyo++os:
              .o:`.syhhhhhhh/.oo++o`
                  /osyyyyyyo++ooo+++/
                      ````` +oo+++o\:
                             `oo++.
            """

    finally:
        file.close()


def find_file():
    top_path = '/home/sdu/Project/crawler/common/crawler/service/apps/inspection/impl'

    all_ = os.walk(top_path)

    result = []

    count_file = 0
    line = 0
    for each in all_:
        current_top_path = each[0]
        current_folder_list = each[1]
        current_file_list = each[2]

        for current_file in current_file_list:
            count_file += 1

            '''得到当前文件路径'''
            current_file_path = '%s%s%s' % (
                current_top_path, os.sep, current_file)

            print '%s > analysis [%s]' % (count_file, current_file_path)

            '''得到当前文件扩展名'''
            current_file_extension = (os.path.splitext(current_file))[1]

            if current_file_extension in ['.py', '.PY']:
                result.append(current_file_path)
    return result

# 读取 excel 表格, 通过读取的数据向数据库查询 level


def readExcel():

    # 打开文件
    workbook = xlrd.open_workbook(r'file/crawler_feedback.xls')

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

    print 'sheetName = %s , rownum = %s, colnum = %s' % (sheetName, rownum, colnum)

    # 获取整行和整列的值（数组）
    list2 = []
    for r in range(1, rownum):
        rowValue = sheet1.row_values(r)
        if rowValue[5] == u'修改抽检单位为简称':
            old_str = rowValue[1]
            new_str = rowValue[3]
            result = find_file()
            for filepath in result:
                rw_file(filepath, old_str, new_str)


def main():
    readExcel()


if __name__ == '__main__':
    main()
