# -*- coding: utf-8 -*-
import time
import datetime
import xlrd
import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from collections import Counter
from mysql import query, query_one, save

"""
INDEX:
    ALTER TABLE base_userpay ADD INDEX user_pay_id (`id`);
    ALTER TABLE base_userpay ADD INDEX user_pay_user_id (`user_id`);
    ALTER TABLE base_userpay ADD INDEX user_pay_shop_id (`shop_id`);
    ALTER TABLE base_userpay ADD INDEX user_pay_time_stamp (`time_stamp`);

    ALTER TABLE base_userview ADD INDEX user_view_id (`id`);
    ALTER TABLE base_userview ADD INDEX user_view_user_id (`user_id`);
    ALTER TABLE base_userview ADD INDEX user_view_shop_id (`shop_id`);
    ALTER TABLE base_userview ADD INDEX user_view_time_stamp (`time_stamp`);

    ALTER TABLE base_shopinfo ADD INDEX shop_info_id (`id`);
    ALTER TABLE base_shopinfo ADD INDEX shop_info_city_name (`city_name`);
    ALTER TABLE base_shopinfo ADD INDEX shop_info_shop_id (`shop_id`);
"""


def handle_data():
    for shop_id in xrange(1, 2001):
        if shop_id % 100 == 0:
            time.sleep(5)

        time_data = []
        time_stamp_data = query(
            sql=u"""SELECT `time_stamp` FROM `base_userview` WHERE `shop_id` = %s LIMIT 0,5""" , list1=(shop_id, ))
        for time_stamp in time_stamp_data:
            time_data.append(time_stamp.get('time_stamp').strftime("%Y-%m-%d"))

        # time_data = sorted(time_data)

        time_data_count_data = dict(Counter(time_data))
        print time_data_count_data
        break

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
    handle_data()


if __name__ == '__main__':
    main()
