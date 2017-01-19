#!/usr/bin/env python
# coding=utf-8

import sys
import MySQLdb
import xlwt
import mysql_2 as mysql

reload(sys)
sys.setdefaultencoding('utf8')
# db=raw_input('请输入数据库名:')
db = 'yqj2'
table = 'risk_news'
# table=raw_input('请输入数据表名:')

select_risk_news = u"""SELECT id, title FROM risk_news"""

def get_risk_news():
    risk_news_data = mysql.query(select_risk_news)
    return

def get_risk_keyword_id():
    ids = []
    data = mysql.query(
        u"""SELECT id FROM risk_keyword where name in('违规','风险','不安全','甲醛含量','污染','危机','曝光','爆炸')""")
    for index in data:
        ids.append(int(index['id']))

    return ids


def filter_keyword():
    keywords1 = [
        u'奥运,得奖,违章,逃逸,肇事,比赛,闯红灯',
        u'交通安全,高速交警,车祸,价格,理财,发行股票',
        u'项目评估,报告,转型',
        u'妙招',
        u'空气',
        u'肖像权',
        u'明星,魔兽,游戏,背景,股份,视频,发布会,造型,写真,娱乐,性感',
        u'炸弹']
    keywords2 = [u'违规', u'风险', u'不安全', u'甲醛含量', u'污染', u'危机', u'曝光', u'爆炸']

    ids = get_risk_keyword_id()

    all_id = []

    ids_len = len(ids)

    for index in xrange(0, ids_len):
        risk_id = []
        k1 = keywords1[index]
        k2 = keywords2[index]

        id1 = ids[index]

        select_risk_news = u"""SELECT id FROM risk_news WHERE title like'%杜森%' """

        k1 = k1.split(',')
        # for k in k1:
        #     select_risk_news += u"""content like %s or """ % ("'%"+k+"%'")

        # select_risk_news += (u"""title like %s  and risk_keyword_id = %s """ % ("'%"+k2+"%'", id1))

        for k in k1:
            select_risk_news += u"""or title like %s """ % ("'%" + k + "%'")

        select_risk_news += u"""  and risk_keyword_id = %s """ % id1

        print select_risk_news

        if index == 2:
            r_id = mysql.query(select_risk_news)
            risk_id3 = []
            risk_id2 = []
            for r in r_id:
                risk_id2.append(int(r['id']))
            for ri in risk_id2:
                title = mysql.query(
                    u'SELECT title FROM risk_news WHERE id = %s' % ri)
                for ti in title:
                    ti = ti['title']
                    if (u'质量' not in ti) and (u'抽检' not in ti) and (u'质检' not in ti) and (u'国家质监总局' not in ti) and (u'质监' not in ti) and (u'抽检' not in ti):
                        print ti
                        risk_id3.append(ri)

            all_id.append(risk_id3)
        else:
            r_id = mysql.query(select_risk_news)

            for r in r_id:
                risk_id.append(int(r['id']))

            all_id.append(risk_id)

    return all_id


def xls():
    # xls info
    try:
        shendu = 0
        wbk = xlwt.Workbook()

        keywords2 = [u'违规', u'风险', u'不安全', u'甲醛含量', u'污染', u'危机', u'曝光', u'爆炸']

        all_risk_id = filter_keyword()

        count = -1
        for i in all_risk_id:
            count += 1
            sheet = wbk.add_sheet(keywords2[count])

            conn = MySQLdb.connect(
                host='192.168.1.205', port=13306, charset='utf8', user='shendu', passwd='P@55word')
            cursor = conn.cursor()
            cursor.execute('use information_schema')
            cursor.execute(
                'select COLUMN_NAME  from COLUMNS where TABLE_NAME=%s and TABLE_SCHEMA=%s', (table, db))
            columnName = cursor.fetchall()
            columnLen = len(columnName)
            columnNum = 0
            for data in range(columnLen):
                sheet.write(0, columnNum, columnName[columnNum][0])
                columnNum += 1
            risk_id_str = ''
            for risk_id in i:
                risk_id_str += ", %s" % risk_id

            cursor.execute(
                'select id ,title,url,pubtime,reprinted ,publisher_id, risk_keyword_id from yqj2.risk_news where id in(1%s)' % risk_id_str)

            dataInfo = cursor.fetchall()
            rowLine = 0
            dataInfo_len = len(dataInfo)
            print dataInfo
            # print mysql.save('DELETE FROM yqj2.risk_news_area WHERE risknews_id IN(1%s)' % risk_id_str)
            # print mysql.save('DELETE FROM yqj2.risk_news_enterprise WHERE risknews_id IN(1%s)' % risk_id_str)
            # print mysql.save('DELETE FROM yqj2.risk_news_industry WHERE
            # risknews_id IN(1%s)' % risk_id_str)
            # print mysql.save('delete from yqj2.risk_news where id in(1%s)' % risk_id_str)
            for line in xrange(dataInfo_len):
                print '此次操作共需向 Excel 写入 %s 行数据, 现已写入 %s 行~~~' % (dataInfo_len, line + 1)
                lineInfo = dataInfo[line]
                rowLine += 1
                columnLine = 0
                shendu += 1
                print 'execute >>> %s ' % shendu
                for row in lineInfo:
                    sheet.write(rowLine, columnLine, row)
                    columnLine += 1
        wbk.save('%s.xls' % table)
    finally:
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    xls()
