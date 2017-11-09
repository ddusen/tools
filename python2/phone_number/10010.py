#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
解决茫茫号码群挑选的繁琐，
帮你轻松选出心仪的号码，
所想即所得。
'''
import sys
import time
sys.path.append('/home/sdu/Project/tools/code/utils/crawler')

from process import get_response
from mysql import query, query_one, save


def save_phone():
	header = {
		'Cookie':'gipgeo=71|710; _n3fa_cid=00f3d758a5314bcdf0563cf8a25851b6; _n3fa_ext=ft=1506245499; _n3fa_lvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1506245499; _n3fa_lpvt_a9e72dfe4a54a20c3d6e671b3bad01d9=1506245499; TC_CD=94921d44-95e1-486e-8e5c-4cd1e3b4c81c; mallcity=51%7C540',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
	}
	index = 0
	while True:
		time.sleep(1)
		index += 1
		r = get_response("https://m.10010.com/NumApp/NumberCenter/qryNum?callback=jsonp_queryMoreNums&provinceCode=51&cityCode=540&monthFeeLimit=0&groupKey=21236872&searchCategory=3&net=01&amounts=200&codeTypeCode=&searchValue=&qryType=02&goodsNet=4&_=150624549923%s" % index, 
			headers=header)

		data = r.text.split(',')
		for d in data:
			if len(d) == 11:
				if not query_one(sql=u'SELECT COUNT(*) FROM `phone_number` WHERE `number`=%s',list1=(d,)).get('COUNT(*)'):
					save(sql=u'INSERT INTO `phone_number`(`number`) VALUES(%s)', list1=(d,))
					print d



def main():
	# 186,185 开头, 不含4
	pn_list = query(sql=u'SELECT * FROM `phone_number` WHERE (`number` LIKE %s OR `number` LIKE %s) AND `number` NOT LIKE %s', list1=('186%', '185%', '%4%', ))
	for p in pn_list:
		print p

if __name__ == '__main__':
	main()