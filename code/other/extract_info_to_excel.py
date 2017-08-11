#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def find_file():
    top_path = raw_input('请输入待查找的初始目录:')
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


def read_file(filepath):
    try:
        file = open(filepath, r'r')
        file.seek(0, 0)
        return file.read()
    finally:
        file.close()


def extract_info(text):
    FirstCrawler_url_pattern = re.compile(r"url = [\'\"](http.*?)[\'\"]")
    ContentCrawler_publisher_pattern = re.compile(r"'publisher': u'(.*?)',")

    url = FirstCrawler_url_pattern.findall(text)
    publisher = ContentCrawler_publisher_pattern.findall(text)

    return(url, publisher)


def write_excel(url_list, publisher_list):
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet('sheet_1', cell_overwrite_ok=True)

    for index, publisher in enumerate(publisher_list):
        # 写入数据table.write(行,列,value) 使用样式
        table.write(index, 1, unicode(publisher, "utf-8"))
        print 'writing data...[%s, %s]' % (1, index)

    for index, url in enumerate(url_list):
        table.write(index, 2, unicode(url, "utf-8"))  # 写入数据table.write(行,列,value) 使用样式
        print 'writing data ...[%s, %s]' % (2, index)

    # 保存文件
    file.save('crawler.xls')


def main():
    file_path_list = find_file()
    url_list = []
    publisher_list = []
    for filepath in file_path_list:
        text = read_file(filepath)
        url = extract_info(text)[0]
        publisher = extract_info(text)[1]
        try:
            url_list.append(url[0])
            publisher_list.append(publisher[0])
        except:
            print filepath

    write_excel(url_list, publisher_list)


if __name__ == '__main__':
    main()
