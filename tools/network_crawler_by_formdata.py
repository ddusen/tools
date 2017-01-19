#!/usr/bin/python
#coding=utf-8
import requests
import MySQL as mysql
import urllib
import urllib2
import cookielib


corpus_words = u"""不合格 不达标 超标 褪色 致癌 危险 异味 PH值 纤维含量 过期 异物 色素 防腐剂 产品质量 抽查 整改 投诉 违规 风险 不安全 甲醛含量 伪冒 劣质 三无 污染 造假 噪音 故障 频发 事故 危机 曝光 预警 召回 爆炸 漏水 燃爆 伤害 自燃"""



def get_id_name():
	'''得到一个字典型数据:
		{'id': 2379L, 'name': u'\u98df\u54c1\u7528\u9676\u74f7\u5236\u54c1'}, {'id': 2380L, 'name': u'\u98df\u54c1\u7528\u6d88\u6bd2\u5242'})
	'''
	select_sql = u'''SELECT id,name FROM industry '''

	sql_data = mysql.query(sql=select_sql)

	return sql_data



def main():

	sql_data = get_id_name()

	filename = 'cookie.txt'

	cookie = cookielib.MozillaCookieJar(filename)

	handler = urllib2.HTTPCookieProcessor(cookie)

	opener = urllib2.build_opener(handler)

	postdata = urllib.urlencode({
			'username':'wuhan',
			'password':'wuhan'
		})


	login_url = 'http://192.168.1.200:8000/admin/login/?next=/admin/'

	result = opener.open(login_url,postdata)

	print result

	cookie.save(ignore_discard=True,ignore_expires=True)

	gradeUrl = 'http://192.168.1.200:8000/admin/corpus/corpus/add/'


	# for each in sql_data:
	# 	each_id = each['id']
	# 	each_name = each['name']
		
	# 	params2 =  { 'riskword':corpus_words,
	# 			'industry':each_id,
	# 			'industry_value':each_name}

	# 	result = opener.open(gradeUrl,params2)

	# 	print result.read()



if __name__ == '__main__':
	main()



