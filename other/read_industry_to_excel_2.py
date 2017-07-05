# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from mysql import query, query_one, save


def get_industry():
    level_three = []
    level_two = []
    level_one = []
    for three in query(sql=u"SELECT * FROM yqj2.industry WHERE level = 3 ORDER BY id"):
        level_three.append(three.get('name'))

        two = query_one(
            sql=u"SELECT * FROM yqj2.industry WHERE id = %s " % three.get('parent_id'))
        level_two.append(two.get('name'))

        one = query_one(
            sql=u"SELECT * FROM yqj2.industry WHERE id = %s " % two.get('parent_id'))
        level_one.append(one.get('name'))

    return(level_one, level_two, level_three)


def write_excel(data):

    level_one, level_two, level_three = data[0], data[1], data[2]

    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet('sheet_1', cell_overwrite_ok=True)

    for index, one in enumerate(level_one):
        table.write(index, 0, one)
        print 'writing data...[%s, %s]' % (0, index)

    for index, two in enumerate(level_two):
        table.write(index, 1, two)
        print 'writing data...[%s, %s]' % (1, index)

    for index, three in enumerate(level_three):
        table.write(index, 2, three)
        print 'writing data...[%s, %s]' % (2, index)

    # 保存文件
    file.save('industry.xls')


def main():
    write_excel(get_industry())

if __name__ == '__main__':
    main()
