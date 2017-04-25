#!/usr/bin/python
#coding=utf-8

import os

'''
	0.编写一个程序, 统计当前目录下每个文件类型的文件数, 程序实现如下:
	dusen@debian:/media/dusen/学习/Python/Learning/030(文件2)$ python count_file_extension.py 
	该文件夹下共有类型为 [.py] 的文件 2 个

'''
def file_path_list():
	path = os.getcwd()

	'得到当前目录下所有文件'
	file_list = os.listdir(path)

	file_path_list = []

	for filename in file_list:
		file_path_list.append('%s%s%s' % (path,os.sep, filename))

	return file_path_list

def count_extension(filepath):
	count_file = []
	for file in filepath:
		file_extension = (os.path.splitext(file))[1]
		count_file.append(file_extension)

	union_extension = list(set(count_file))

	for index in union_extension:
		count  = 0
		for each in count_file:
			if each == index :
				count += 1
		print '该文件夹下共有类型为 [%s] 的文件 %s 个' % (index,count)


def main():
	count_extension(file_path_list())


if __name__ == '__main__':
	main()

