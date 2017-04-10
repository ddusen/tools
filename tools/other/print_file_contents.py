#!/usr/bin/python
#coding=utf-8

'''
	2. 编写一个程序, 当用户输入文件名和行数(N) 后, 将该文件的前 N 行内容打印到屏幕上, 程序实现如下:

	dusen@debian:/media/dusen/学习/Python/Learning/029(文件1)$ python MoveHands_02.py 
	>>>	请输入要打开的文件(/home/test.txt):1.t  
	>>>	请输入需要显示该文件前几行:45
	>>>	[Errno 2] No such file or directory: '1.t'
	>>>	-_-您的输入有误,请重试!
	>>>	请输入要打开的文件(/home/test.txt):1.txt
	>>>	请输入需要显示该文件前几行:5
	>>>	文件 1.txt 的前 5 行的内容如下:
	>>>	fdhjsaklhflakjsdfhalsd

	>>>	hfdljaskhflaskdjhf

	>>>	hfajlksdld

	>>>	hfljkasd

	>>>	hfajds


'''

def read_file(filename,line_number):
	file = open(filename,'r')
	file.seek(0,0)
	print '文件 %s 的前 %s 行的内容如下:' % (filename,line_number)
	for index in range(int(line_number)):
		print file.readline()


def main():
	try:
		filename = raw_input('请输入要打开的文件(/home/test.txt):')
		line_number = raw_input('请输入需要显示该文件前几行:')	
		read_file(filename,line_number)

	except Exception ,e:
		print e
		print '-_-您的输入有误,请重试!'
		main()


if __name__ == '__main__':
	main()
