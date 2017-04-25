#!/usr/bin/python
# -*- coding: utf-8 -*-
import xlwt

from mysql import query, query_one, save


def export():
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet('sheet_1', cell_overwrite_ok=True)


    for i in range(1, 96):
        level_one_data = query(sql=u"SELECT * FROM product WHERE id = %s ORDER BY code DESC" , list1=(i, ))
        for one, level_one in enumerate(level_one_data):
            level_one_name = level_one.get("name")
            level_one_id = level_one.get("id")

            level_two_data = query(sql=u"SELECT * FROM product WHERE parent_id = %s" , list1=(level_one_id, ))
            for two, level_two in enumerate(level_two_data):
                level_two_name = level_two.get("name")
                level_two_id = level_two.get("id")
                
                level_three_data = query(sql=u"SELECT * FROM product WHERE parent_id = %s" , list1=(level_two_id, ))
                for three, level_three in enumerate(level_three_data):
                    level_three_name = level_three.get("name")
                    level_three_id = level_three.get("id")
                    table.write((one + 1 * two + 1 * three + 1), 0, level_one_name)
                    table.write((one + 1 * two + 1 * three + 1), 1, level_two_name)
                    table.write((one + 1 * two + 1 * three + 1), 2, level_three_name)


    # 保存文件
    file.save('/home/sdu/MyProject/tools/tools/product/test.xls')


def main():
    export()



if __name__ == '__main__':
    main()
