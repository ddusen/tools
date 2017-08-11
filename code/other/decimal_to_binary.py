#coding=utf-8

'''
	0. 编写一个进制转换程序 (提示，十进制转换二进制可以用bin()这个BIF）：
'''

while True:
	print '----------------------------------------我是分割线宝宝(begin)------------------------------------------'
	temp_1 = raw_input('请输入你要转换的数字(输入 q 退出程序):\n')

	if temp_1 == 'q':
		print '退出成功, 欢迎再次使用!'
		break

	temp_2 = raw_input(
	'''请选择你要转化的进制(输入 q 退出程序):
	1 > 二进制
	2 > 八进制
	3 > 十进制
	4 > 十六进制\n''')

	if temp_2 == "q":
		print '退出成功, 欢迎再次使用!'
		break

	try:
		num = int(temp_1)
		ary = int(temp_2)

		if ary == 1:
			print '转换后的结果: %s ' % bin(num)
		elif ary == 2 :
			print '转换后的结果: %o ' % num
		elif ary == 3 :
			print '转换后的结果: %d ' % num 
		elif ary == 4 :
			print '转换后的结果: %x ' % num 
		else:
			print '本宝宝才华有限, 只能进行以上四种转换~~~'

	except:
		print '输入有误, 本宝宝只接受数字~~~'

	print '----------------------------------------我是分割线宝宝(end)------------------------------------------'
	