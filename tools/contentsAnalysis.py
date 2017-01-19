#!/usr/bin/python 
#coding=utf-8

import os

def dirList(path):
	fileList = os.listdir(path)
	filePath = os.getcwd()
	allFile = []
	for fileName in fileList:
		filePath = os.path.join(filePath, fileName)
		if os.path.isdir(filePath):
			dirList(filePath)
		allFile.append(filePath)
	return allFile



if __name__ == '__main__':
	path = raw_input('请输入文件路径:')
	if path == '':
		path = '/home/dusen/Python'
 	allFile = dirList(path)
 	print allFile 