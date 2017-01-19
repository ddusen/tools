#!/usr/bin/python
# coding=utf-8

import os

'''
	4. 编写一个程序, 用户输入关键字,查找当前文件内(如果当前文件夹包含文件夹, 则进入文件夹继续搜索)所有含有该关键字的文本文件(.txt后缀),
	要求显示该文件所在位置以及关键字在文件内的具体位置(第几行第几个字符)程序实现如下:



'''


def read_file(filepath, keyword):
    file = open(filepath, 'r')
    file.seek(0, 0)

    '行数'
    count_line = 0

    result = []
    if keyword in file.read():
        result.append('=' * 80)
        result.append('->在文件 [%s] 中找到关键字 [%s] ' % (filepath, keyword))

        file.seek(0, 0)

        for file_line in file:
            count_line += 1
            if keyword in file_line:
                result.append('-->关键字出现在第 %s 行' % [count_line])

    file.close()
    return result


def find_file():
    top_path = raw_input('请输入待查找的初始目录:')
    keyword = raw_input('请输入关键字:')

    all_ = os.walk(top_path)

    result = []

    count_folder = 0
    count_file = 0
    line = 0
    for each in all_:
        current_top_path = each[0]
        current_folder_list = each[1]
        current_file_list = each[2]

        count_folder += 1

        for current_file in current_file_list:
            count_file += 1

            '得到当前文件路径'
            current_file_path = '%s%s%s' % (
                current_top_path, os.sep, current_file)

            print '%s > analysis [%s]' % (count_folder, current_file_path)

            '得到当前文件扩展名'
            current_file_extension = (os.path.splitext(current_file))[1]

            if current_file_extension in ['.txt', '.TXT']:
                result2 = read_file(current_file_path, keyword)
                if result2 != None:
                    for index in result2:
                        result.append(index)

    print '本次操作共分析 %s 个文件夹, %s 个文件' % (count_folder, count_file)
    return result


def main():
    try:
        result = find_file()
        if result:
            print '结果如下:[ \n'
            for index in result:
                print index
            print '\n ]'
        else:
            print '初始目录下所有文件中没有发现此关键字'
    except Exception, e:
        print e
        # main()

if __name__ == '__main__':
    main()
