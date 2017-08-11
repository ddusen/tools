#coding=utf-8
'''
	0. 请写一个密码安全性检查的脚本代码：check.py
	  
	 密码安全性检查代码
	
	 低级密码要求：
	   1. 密码由单纯的数字或字母组成
	   2. 密码长度小于等于8位
	
	 中级密码要求：
	   1. 密码必须由数字、字母或特殊字符（仅限：~!@$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
	   2. 密码长度不能低于8位
	
	 高级密码要求：
	   1. 密码必须由数字、字母及特殊字符（仅限：~!@$%^&*()_=-/,.?<>;:[]{}|\）三种组合
	   2. 密码只能由字母开头
	   3. 密码长度不能低于16位
'''


symbols = r'''`!@#$%^&*()_+-=/*{}[]\|'";:/?,.<>'''
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'

while True:
	temp = raw_input('请输入你要检查的密码(退出请输入 q ): ')
	if temp == 'q' :
		print '执行了您的退出指令...'
		break

	try:
		password = str(temp)

		flag_len = 0
		password_len = len(password)
		if 0 < password_len <= 8:
			flag_len = 1
		elif 8 <= password_len <= 16 :
			flag_len = 2
		else :
			flag_len = 3


		flag_con = 0
		for each in password:
			if each in symbols:
				flag_con += 1
				break
		for each in password :
			if each in chars:
				flag_con += 1
				break
		for each in nums:
			if each in nums:
				flag_con += 1
				break


		# 低级密码
		if flag_con == 1 or flag_len == 1 :
			print  '低级密码'
			continue
		elif flag_con == 2 or flag_len == 2:
			print '中级密码'
			continue
		else :
			print '高级密码'
			continue

	except Exception :
		print '系统内部错误,退出程序!'
		break

