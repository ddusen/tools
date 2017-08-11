# -*- coding: utf-8 -*-
import time
import datetime as datetime2
import csv

from datetime import datetime, date, timedelta
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


def get_time_sequence():
    time_sequence_list = []

    def date_range(start, stop, step):
        while start < stop:
            yield start
            start += step

    for d in date_range(datetime(2015, 6, 25), datetime(2016, 11, 1), timedelta(hours=24)):
        time_sequence_list.append(str(d)[0:10])

    return time_sequence_list


def handle_data(time_sequence_list):

    with open('/home/sdu/MyProject/tools/tools/tianchi/data2.csv', 'wb') as csvfile:
        spamwriter = csv.writer(csvfile)
        index = 0
        for time_date in time_sequence_list:
            starttime = datetime2.datetime.now()
            row_data = []

            if index == 0:
                row_data = range(1, 2001)
                spamwriter.writerow([""] + row_data)
                index += 1
                continue
            else:
                for shop_id in xrange(1, 2001):
                    time_sequence_dict = query(
                        sql=u"""SELECT LEFT(`time_stamp`,10) FROM `base_userpay` WHERE `shop_id` = %s AND `time_stamp` LIKE '%s%%' """ % (shop_id, time_date))

                    if not time_sequence_dict:
                        row_data.append("0")
                    else:
                        row_data.append(len(time_sequence_dict))

            endtime = datetime2.datetime.now()
            print "EXECUTE < %s > ROW SUCCESS, EXECUTION TIME < %s > !" % (index, (endtime - starttime).seconds)
            index += 1
            spamwriter.writerow([time_date] + row_data)


def main():
    time_sequence_list = get_time_sequence()
    handle_data(time_sequence_list)


if __name__ == '__main__':
    main()
