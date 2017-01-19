#!/usr/bin/python
#coding=utf-8

import os

'''
	0. 编写一个程序, 接受用户的输入并保存为新的文件, 程序的实现如下:
	
	>>>	请输入文件名:1.txt
	>>>	当前目录[/media/dusen/学习/Python/Learning/029(文件1)]下存在同名文件, 
	>>>	请重新输入文件名:2.txt
	>>>	请输入内容[单独输入':w'保存退出]:
	>>>	fdhjsaklhflakjsdfhalsd
	>>>	hfdljaskhflaskdjhf
	>>>	hfajlksdl
	>>>	hfljkasd
	>>>	hfajds
	>>>	hfalkjsd
	>>>	hfadjs
	>>>	hfadsj
	>>>	hjkfads
	>>>	hajflsd
	>>>	hafjkds
	>>>	hjklafsd
	>>>	hfalds
	>>>	hdfljkas:w
	>>>	faj;skd
	>>>	:w
	>>>	成功保存文件到 [/media/dusen/学习/Python/Learning/029(文件1)] 目录^_^!


'''

def save_file(filename):
	try:
		filepath = '%s/%s' % (os.getcwd(),filename)
		file = open(filepath,'r')
		filename = raw_input( '当前目录[%s]下存在同名文件, \n请重新输入文件名:' % os.getcwd())
		save_file(filename)
		file.close()
	except:
		print '请输入内容[单独输入\':w\'保存退出]:'
		text = ''
		file = open(('%s/%s' % (os.getcwd(),filename)),'w')
		while text != ':w':
			text = raw_input('')
			if text != ':w':
				file.write(text)
				file.write('\n')
		file.close()
		print '成功保存文件到 [%s] 目录^_^!' % os.getcwd()



def main():
	filename = raw_input('请输入文件名:')
	save_file(filename)



if __name__ == '__main__':
	main()