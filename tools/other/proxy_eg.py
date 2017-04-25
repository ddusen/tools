#!/usr/bin/python
#coding=utf-8

import urllib.request
import random

def main():
	try:
		while True:

			url = 'http://www.ip138.com/'

			ip_list = ['218.75.100.114:8080','211.167.248.228:8080','60.12.227.208:80']

			"""代理步骤:
			1. 参数是一个字典{'类型':'代理 ip:端口号'}"""
			proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})

			'2.定制，创建一个　opener'
			opener = urllib.request.build_opener(proxy_support)
			opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36')]


			'3a.安装 opener'
			urllib.request.install_opener(opener)

			'3b.调用 opener'
			response = urllib.request.urlopen(url)

			html = response.read().decode('utf-8')

			print(html)

	except:
		main()


if __name__ == '__main__':
	main()
