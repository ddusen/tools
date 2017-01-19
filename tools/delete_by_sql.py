# -*- coding: utf-8 -*-
import mysql

selete_sql = u"""select url  from crawler.crawler_task where sub_app = 'zjld' and app = "observer" and status = 2 and last_run < now()"""
delete_sql = u"""delete from yqj.article where url = %s"""


def main():
	url_list = mysql.query(sql=selete_sql)
	for url in url_list:
		result = mysql.save(sql=delete_sql, list1=(url.get("url")))
		print "%s delete %s success !" % (result, url['url'])


if __name__ == '__main__':
	main()
