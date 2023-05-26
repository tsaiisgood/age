password = 'a123456'
i=3
while True:
	pwd = input('輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		i = i -1
		print('密碼錯誤剩下', i ,'次')
		if i == 0:
			break