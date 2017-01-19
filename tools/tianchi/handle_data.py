# -*- coding: utf-8 -*-
import time
import datetime
import csv

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
    with open('data.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)

        for shop_id in xrange(1, 2001):
            if shop_id % 100 == 0:
                time.sleep(5)

            time_data = []
            time_stamp_data = query(
                sql=u"""SELECT `time_stamp` FROM `base_userview` WHERE `shop_id` = %s """ , list1=(shop_id, ))
            for time_stamp in time_stamp_data:
                time_data.append(time_stamp.get(
                    'time_stamp').strftime("%Y-%m-%d"))

            time_data_count_data = dict(Counter(time_data))

            time_data_count_data = sorted(
                time_data_count_data.iteritems(), key=lambda d: d[0])

            datetime = []
            datetime_count = []

            for data in time_data_count_data:
                if shop_id == 1:
                    datetime.append(data[0])

                datetime_count.append(data[1])


            if shop_id == 1:
                spamwriter.writerow(datetime)
                spamwriter.writerow(datetime_count)
            else:
                spamwriter.writerow(datetime_count)

            print shop_id

def main():
    handle_data()


if __name__ == '__main__':
    main()
