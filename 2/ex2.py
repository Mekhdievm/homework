def ex2():
	res = 0
	while 1:
		print('Введите число:')
		num = int(input())
		res += num
		if (num == 0):
			return res

print(ex2())