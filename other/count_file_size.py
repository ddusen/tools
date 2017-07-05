#!/usr/bin/python
#coding=utf-8

import os

'''
	1.编写一个程序, 计算当前文件夹下所有文件的大小 程序实现如下:
	
	>>>	dusen@debian:/media/dusen/学习/Python/Learning/030(文件2)$ python count_file_size.py 
	>>>	count_file_extension.py  [1015Bytes]
	>>>	count_file_size.py  [645Bytes]
	
'''
def file_path_list():
	path = os.getcwd()

	'得到当前目录下所有文件'
	file_list = os.listdir(path)

	file_path_list = []

	for filename in file_list:
		file_path_list.append('%s%s%s' % (path,os.sep, filename))

	return file_path_list

def count_file_size(filepath):
	for file in filepath:
		filename = os.path.basename(file)
		filesize = os.path.getsize(file)
		print '%s  [%sBytes]' % (filename,filesize)

def main():
	count_file_size(file_path_list())


if __name__ == '__main__':
	main()

