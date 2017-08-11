#!/usr/bin/python
#coding=utf-8

import os

'''
	2. 编写一个程序, 用户输入文件名以及开始搜索的路径, 搜索该文件是否存在. 如果遇到文件夹, 则进入文件夹继续搜索,程序实现如下:

	>>>	dusen@debian:/media/dusen/学习/Python/Learning/030(文件2)$ python find_file.py 
	>>>	请输入待查找的初始目录:/home/dusen/shendu
	>>>	请输入需要查找的目录文件:manage.py
	>>>	1 > analysis [/home/dusen/shendu]
	>>>	2 > analysis [/home/dusen/shendu/crawler]
	>>>	3 > analysis [/home/dusen/shendu/crawler/common]
	>>>	4 > analysis [/home/dusen/shendu/crawler/common/crawler]
	>>>	...
	>>>	125 > analysis [/home/dusen/shendu/inspection/.git/objects]
	>>>	126 > analysis [/home/dusen/shendu/inspection/.git/objects/info]
	>>>	127 > analysis [/home/dusen/shendu/inspection/.git/objects/pack]
	>>>	128 > analysis [/home/dusen/shendu/inspection/.git/hooks]
	>>>	129 > analysis [/home/dusen/shendu/inspection/.git/branches]
	>>>	本次操作共分析 129 个文件夹, 594 个文件
	>>>	结果如下:[ 

	>>>	/home/dusen/shendu/crawler/common/manage.py
	>>>	/home/dusen/shendu/inspection/common/manage.py

 	>>>	]



'''
def find_file():
	top_path = raw_input('请输入待查找的初始目录:')
	file_name = raw_input("请输入需要查找的目录文件:")
	os.chdir(top_path)

	all_ =  os.walk(top_path)

	result = []

	count_folder = 0
	count_file = 0
	for each in all_:
		current_top_path = each[0]
		current_folder_list = each[1]
		current_file_list = each[2]

		count_folder += 1
		print '%s > analysis [%s]' % (count_folder,current_top_path)

		for current_file in current_file_list:
			count_file += 1
			if current_file == file_name :
				result.append('%s%s%s' % (current_top_path,os.sep,current_file))

	print '本次操作共分析 %s 个文件夹, %s 个文件' % (count_folder,count_file)
	return result


def main():
	try:
		result = find_file()
		if result :
			print '结果如下:[ \n'
			for index in result:

				print index
			print '\n ]'
		else:
			print '初始目录下没有发现该文件'
	except Exception ,e:
		print e
		main()

if __name__ == '__main__':
	main()

