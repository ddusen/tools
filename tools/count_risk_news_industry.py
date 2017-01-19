# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from mysql import query, query_one, save


def get_industry():
    level_3_industry_count = {}
    level_1_id_data = {1854: u'日用消费品', 2087: u'建筑装饰装修材料',
                       2144: u'工业生产资料', 2323: u'农业生产资料', 2343: u'食品相关产品'}

    level_1_id = u'2343'

    level_2_ids = query(
        sql="SELECT id FROM yqj2.industry WHERE parent_id = %s AND level=2" % level_1_id)
    for ids in level_2_ids:
        level_3 = query(
            sql="SELECT * FROM yqj2.industry WHERE parent_id = %s AND level=3" % ids.get('id'))

        for l3 in level_3:
            level_3_id = l3.get('id')
            level_3_name = l3.get('name')

            industry_risk_news_count = query(
                sql=u"SELECT COUNT(*) FROM yqj2.risk_news_industry WHERE industry_id = %s " % level_3_id)
            level_3_industry_count[level_3_name] = int(
                industry_risk_news_count[0].get('COUNT(*)'))

    return level_3_industry_count


def write_excel(industry_count_data):
    file = xlwt.Workbook()                # 注意这里的Workbook首字母是大写
    table = file.add_sheet('sheet_1', cell_overwrite_ok=True)
    index = 0
    for k, v in industry_count_data.items():
        table.write(index, 1, k)
        table.write(index, 2, v)
        print 'writing data... <%s, %s>' % (k, v)
        index += 1

    # 保存文件
    file.save('level3_industry_risk_news_count.xls')


def main():
    write_excel(get_industry())

if __name__ == '__main__':
    main()
