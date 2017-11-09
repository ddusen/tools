#!/usr/bin/python3

import os, sys
sys.path.append(os.getcwd())

from utils.db.mysql import query, query_one, save
from utils.office.excel import write_xlsx


def db_config():
    return {
        'host':'192.168.1.205',
        'port':13306,
        'user':'shendu',
        'passwd':'P@55word',
        'db':'yqj2'
    }


def risk_news():
    year = 2017
    # monthly news of all status
    monthly1 = query(sql='''SELECT COUNT(*) AS count, MONTH(`pubtime`) AS monthly 
                            FROM `risk_news`
                            WHERE YEAR(`pubtime`)=%s
                            GROUP BY monthly''', 
                        list1=(year, ), 
                        db_config=db_config())

    # monthly news of 2 status
    status = 2
    monthly2 = query(sql='''SELECT COUNT(*) AS count, MONTH(`pubtime`) AS monthly 
                            FROM `risk_news`
                            WHERE `is_delete`=%s AND YEAR(`pubtime`)=%s
                            GROUP BY monthly''', 
                        list1=(status, year, ), 
                        db_config=db_config())

    # weekly news of all status
    weekly1 = query(sql='''SELECT COUNT(*) AS count, 
                                WEEK(`pubtime`) AS weekly, 
                                DATE_FORMAT(`pubtime`, '%%Y-%%m-%%d') AS start_at, 
                                DATE_FORMAT(DATE_ADD(`pubtime`, INTERVAL 6 DAY), '%%Y-%%m-%%d') AS end_at
                            FROM `risk_news`
                            WHERE YEAR(`pubtime`)=%s
                            GROUP BY weekly''',
                        list1=(year, ), 
                        db_config=db_config())

    # weekly news of 2 status
    weekly2 = query(sql='''SELECT COUNT(*) AS count, 
                                WEEK(`pubtime`) AS weekly, 
                                DATE_FORMAT(`pubtime`, '%%Y-%%m-%%d') AS start_at, 
                                DATE_FORMAT(DATE_ADD(`pubtime`, INTERVAL 6 DAY), '%%Y-%%m-%%d') AS end_at
                            FROM `risk_news`
                            WHERE `is_delete`=%s AND YEAR(`pubtime`)=%s
                            GROUP BY weekly''', 
                        list1=(status, year, ), 
                        db_config=db_config())

    return {'monthly1': monthly1,
            'monthly2': monthly2,
            'weekly1': weekly1,
            'weekly2': weekly2}


def origin_inspection():
    year = 2017
    # monthly origin_inspection
    monthly = query(sql='''SELECT COUNT(*) AS count, MONTH(`pubtime`) AS monthly 
                                FROM `origin_inspection`
                                WHERE YEAR(`pubtime`)=%s
                                GROUP BY monthly''', 
                            list1=(year, ), 
                            db_config=db_config())

    # weekly origin_inspection
    weekly = query(sql='''SELECT COUNT(*) AS count, 
                                WEEK(`pubtime`) AS weekly, 
                                DATE_FORMAT(`pubtime`, '%%Y-%%m-%%d') AS start_at, 
                                DATE_FORMAT(DATE_ADD(`pubtime`, INTERVAL 6 DAY), '%%Y-%%m-%%d') AS end_at
                            FROM `origin_inspection`
                            WHERE YEAR(`pubtime`)=%s
                            GROUP BY weekly''',
                        list1=(year, ), 
                        db_config=db_config()) 


    return {'monthly': monthly,
            'weekly': weekly,}


def main():
    filepath = '/home/sdu/Documents/tools/python3/yqj2/2017年抽检数据情况(周统计).xlsx'

    origin_inspection_dict = origin_inspection()
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年抽检数据情况(周统计).xlsx', origin_inspection_dict.get('weekly'))
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年抽检数据情况(月统计).xlsx', origin_inspection_dict.get('monthly'))

    risk_news_dict = risk_news()
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年风险新闻数据情况(周统计).xlsx', risk_news_dict.get('weekly1'))
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年风险新闻数据情况(周统计)2.xlsx', risk_news_dict.get('weekly2'))
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年风险新闻数据情况(月统计).xlsx', risk_news_dict.get('monthly1'))
    write_xlsx('/home/sdu/Documents/tools/python3/yqj2/2017年风险新闻数据情况(月统计)2.xlsx', risk_news_dict.get('monthly2'))


if __name__ == '__main__':
    main()
