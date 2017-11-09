#!/usr/bin/python
#coding=utf-8
import re
'''
	2. 编写一个程序, 当用户输入文件名和行数(N) 后, 将该文件的前 N 行内容打印到屏幕上, 程序实现如下:
	3.扩展: 用户可以随意输入需要显示的行数. (输入 13:21打印第13 行到第21行 输入:21打印前21行, 输入21: 
	从第21行开始到文件结尾)


'''

def read_file(filename,line_number):
	file = open(filename,'r')
	file.seek(0,0)
	line = line_number.split(':')
	prefix = line[0]
	suffix = line[1]
	print '文件 %s 的第 %s 行到第 %s 行的内容如下:' % (filename,prefix,suffix)

	all_line = len(re.findall('\n',file.read()))

	file.seek(0,0)
	if prefix == '':
		prefix = 0
	if suffix == '':
		suffix = all_line

	for index in xrange(int(prefix),int(suffix)):

		print file.readline()


def main():
	try:
		filename = raw_input('请输入要打开的文件(/home/test.txt):')
		line_number = raw_input('请输入需要显示的行数[格式如 13:21 或 :21 或 21:]:')	
		read_file(filename,line_number)

	except Exception ,e:
		print e
		print '-_-您的输入有误,请重试!'
		main()


if __name__ == '__main__':
	main()
