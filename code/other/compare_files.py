#!/usr/bin/python
#coding=utf-8
import os
'''
	1. 编写一个程序, 比较用户输入的两个文件, 如果不同,显示出所有不同处的行号和第一个不同字符的位置, 实现如下:

	>>>	请输入需要比较的头一个文件名:1.tr
	>>>	请输入需要比较的另一个文件名:2.txt
	>>>	>>>
	>>>	-_-文件未找到
	>>>	您当前所在路径是[/media/dusen/学习/Python/Learning/029(文件1)].
	>>>	可能是当前路径下没有你要找的文件
	>>>	你可以切换路径运行本程序~~~
	>>>	<<<
	>>>	请输入需要比较的头一个文件名:1.txt
	>>>	请输入需要比较的另一个文件名:2.txt
	>>>	两个文件共 [3] 处不同:
	>>>	第 3 行不一样
	>>>	第 6 行不一样
	>>>	第 12 行不一样


'''

def read_file():
	log = []	
	file1 = raw_input('请输入需要比较的头一个文件名:')
	file2 = raw_input('请输入需要比较的另一个文件名:')
	file1_path = '%s/%s' % (os.getcwd(),file1)
	file2_path = '%s/%s' % (os.getcwd(),file2)

	f1 = open(file1_path,'r')
	f2 = open(file2_path,'r')
	f1.seek(0,0)
	f2.seek(0,0)
	
	count = 0

	for f1_line in f1:
		count +=1
		f2_line = f2.readline()
		if f1_line != f2_line:
			log.append('第 %s 行不一样' % count)

	return log



def main():
	try:
		log = read_file()
		log_len = len(log)
		print '两个文件共 [%s] 处不同:' % log_len
		for each in log:
			print each
	except:
		print '>>>\n-_-文件未找到\n您当前所在路径是[%s].\n可能是当前路径下没有你要找的文件\n你可以切换路径运行本程序~~~\n<<<' % os.getcwd()
		main()

if __name__ == '__main__':
	main()