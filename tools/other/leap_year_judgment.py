#coding=utf-8
# 1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）
# 这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。


while True:
	temp = raw_input('请输入一个年份: ')

	if not temp.isdigit():
		print '您应该输入一个整数, 请重试...'
		continue
	else:
		year = int(temp)
		if ((year % 4 == 0 ) and (year % 100 != 0)) or (year % 400 == 0):
			print '您输入的年份 %s 是闰年!' % year
		else:
			print '您输入的年份 %s 不是闰年!' % year