#!/usr/bin/python3

from mysql import query, query_one, save


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

    # monthly news of 1 status
    status = 1
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

    # weekly news of 1 status
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
    pass

    
if __name__ == '__main__':
    main()
