#!/usr/bin/python3
#coding=utf-8

import urllib.request
import urllib.parse
import json
import time


def main():
	'基于有道翻译的小程序'
	temp = ''

	try:
		while True:

			temp = input('请输入你要翻译的内容(退出[Q/q]):')

			if temp in ['q','Q']:
				print ('退出成功!')
				break

			url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=baidu'

			"""
			添加 User-Agent 方法一:
			head = {}
			head['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
			"""

			data = {}

			data['type'] = 'AUTO'
			data['i'] = temp
			data['doctype'] = 'json'
			data['xmlVersion'] = '1.8'
			data['keyfrom'] = 'fanyi.web'
			data['ue'] = 'UTF-8'
			data['action'] = 'FY_BY_CLICKBUTTON'
			data['typoResult'] = 'true'


			data = urllib.parse.urlencode(data).encode('utf-8')

			req = urllib.request.Request(url,data)

			'添加 User-Agent 方法二'
			req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')

			response = urllib.request.urlopen(req)

			html = response.read().decode('utf-8')

			target = json.loads(html)

			print ('翻译结果: %s ' % target['translateResult'][0][0]['tgt'])	

			'sleep 1 秒'
			#time.sleep(1)

	except:
		print ('系统内部错误, 请重试!')
		main()




if __name__ == '__main__':
	main()
