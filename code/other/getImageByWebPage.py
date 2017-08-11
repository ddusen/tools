#!/usr/bin/python
#coding=utf-8

import re
import urllib

def getHtml(url):
	'''传入url地址,得到整个页面'''
	html = ''
	print 'Analyzing...'
	try:
		page = urllib.urlopen(url)
		html = page.read()
		print 'Analysis of success!'
	except Exception,e:
		print '传入的url地址不合法,请重新启动程序!'
	finally:
		return html



def  getImage(html):
	'''通过得到的 html 页面, 分析其中的 Image url'''
	image_list = []
	try:
		reg = r'src="(.*?\.jpg)" width='
		image_re = re.compile(reg)
		image_list = re.findall(image_re, html)
		name = 0
		for index in image_list:
			print '正在下载第 %s 个图片!' % (name + 1)
			urllib.urlretrieve(index, '%s.jpg' % name )
			name += 1
		print '一共下载了 %s 个图片到您的电脑^_^' % name
	except Exception, e:
		print '从当前页面获取 jpg 类型的图片失败-_-'
	finally:
		return image_list






if __name__ == '__main__':
	url = raw_input('请输入一个url:')
	if url == '':
		url = 'http://tieba.baidu.com/p/4677372508'
	html = getHtml(url)
	if html != '':
		image_list = getImage(html)
