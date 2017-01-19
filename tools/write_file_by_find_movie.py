#!/usr/bin/python
#coding=utf-8

import os

'''
	3. 编写一个程序, 用户输入开始搜索的路径, 查找该路径下(包含子文件夹内)所有的视频格式文件(要求查找mp4,
	rmvb,avi的格式即可),并创建一个文件(videoList.txt)存放所有找到的文件的路径,程序实现如下:

	>>>	dusen@debian:/media/dusen/学习/Python/Learning/030(文件2)$ python write_file_by_find_movie.py
	>>>	请输入待查找的初始目录:/home/dusen/shendu
	>>>	请输入需要查找的目录文件:manage.py
	>>>	1 > analysis [/home/dusen/shendu]
	>>>	2 > analysis [/home/dusen/shendu/crawler]
	>>>	3 > analysis [/home/dusen/shendu/crawler/common]
	>>>	4 > analysis [/home/dusen/shendu/crawler/common/crawler]
	>>>	...
	>>>	75834 > analysis [/opt/kingsoft/wps-office/office6/qt/plugins/]
	>>>	75835 > analysis [/opt/kingsoft/wps-office/office6/qt/plugins/imageformats/]
	>>>	75836 > analysis [/opt/kingsoft/wps-office/office6/qt/plugins/codecs/]
	>>>	75837 > analysis [/opt/kingsoft/wps-office/office6/qt/plugins/phonon_backend/]
	>>>	75838 > analysis [/opt/kingsoft/wps-office/office6/dicts/]
	>>>	75839 > analysis [/opt/kingsoft/wps-office/office6/dicts/en_US/]
	>>>	本次操作共分析 75839 个文件夹, 517534 个文件
	>>>	结果如下:[ 

	>>>	/home/dusen/Videos/海贼王特别篇：黄金之心.720P.HD中字.mkv
	>>>	/media/dusen/办公/(^_^)(^0^)/大一下学期/思想品德/新闻播报/欧洲多国遭遇强雾霾袭击 伦敦再现雾都景象(图)-空气质量-雾霾_新浪新闻_0.mp4
	>>>	/media/dusen/办公/.Trash-1000/files/a.mp4
	>>>	/media/dusen/办公/Galaxy s6 edge+ 备份/2016央视春晚HDTV_A[电影天堂www.dy2018.com].mkv
	>>>	...
	>>>	media/dusen/学习/学习视频/Python学习视频/01.1.零基础入门学习Python/056轮一只爬虫的自我修养4：OOXX/056轮一只爬虫的自我修养4：OOXX/056轮一只爬虫的自我修养4：OOXX.mp4
	>>>	/media/dusen/学习/学习视频/Python学习视频/01.1.零基础入门学习Python/057论一只爬虫的自我修养5：正则表达式/057论一只爬虫的自我修养5：正则表达式.mp4
	>>>	/media/dusen/学习/学习视频/Python学习视频/01.1.零基础入门学习Python/058论一只爬虫的自我修养6：正则表达式2/058论一只爬虫的自我修养6：正则表达式2.mp4
	>>>	/media/dusen/学习/学习视频/Python学习视频/01.1.零基础入门学习Python/059论一只爬虫的自我修养7：正则表达式3/059论一只爬虫的自我修养7：正则表达式3.mp4

	>>>	 ]
	>>>	此结果正在为你写入到[/media/dusen/学习/Python/Learning/030(文件2)/videoList.txt]文件中...
	>>>	写入完成^-^


'''
def find_movie():
	top_path = raw_input('请输入待查找的初始目录:')

	all_ =  os.walk(top_path)

	result = []

	count_folder = 0
	count_file = 0
	for each in all_:
		current_top_path = each[0]
		current_folder_list = each[1]
		current_file_list = each[2]

		count_folder += 1
		print '%s > analysis [%s%s]' % (count_folder,current_top_path,os.sep)

		for current_file in current_file_list:
			count_file += 1

			'得到当前文件扩展名'
			current_file_extension = (os.path.splitext(current_file))[1]

			if current_file_extension in ['.mp4','.MP4','.rmvb','.RMVB','.avi','.AVI','.mkv','.MKV'] :
				result.append('%s%s%s' % (current_top_path,os.sep,current_file))

	print '本次操作共分析 %s 个文件夹, %s 个文件' % (count_folder,count_file)
	return result


def write_file(data,filepath):
	file = open(filepath,'w')
	file.writelines(data)
	print '写入完成^-^'

def main():
	try:
		result = find_movie()
		if result :
			print '结果如下:[ \n'
			for index in result:

				print index
			print '\n ]'
			file_store_path = '%s%svideoList.txt' % (os.getcwd(),os.sep)
			print '此结果正在为你写入到[%s]文件中...' % file_store_path
			write_file(data=result,filepath=file_store_path)
		else:
			print '初始目录下没有发现视频文件'
	except Exception ,e:
		print e
		main()

if __name__ == '__main__':
	main()

