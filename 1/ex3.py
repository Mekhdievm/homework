def ex3():
    
	print('Введите день:')
	day =  int(input())
	print('Введите месяц:')
	month =  input()
	
	if month == 'март':
		if day < 22:
			return 'Ваш знак зодиака: Рыба'
		else:
			return 'Ваш знак зодиака: Овен'
	elif month == 'апрель':
		if day < 22:
			return 'Ваш знак зодиака: Овен'
		else:
			return 'Ваш знак зодиака: Телец'
	elif month == 'май':
		if day < 22:
			return 'Ваш знак зодиака: Телец'
		else:
			return 'Ваш знак зодиака: Близнецы'
	elif month == 'июнь':
		if day < 22:
			return 'Ваш знак зодиака: Близнецы'
		else:
			return 'Ваш знак зодиака: Рак'
	elif month == 'июль':
		if day < 22:
			return 'Ваш знак зодиака: Рак'
		else:
			return 'Ваш знак зодиака: Лев'
	elif month == 'август':
		if day < 22:
			return 'Ваш знак зодиака: Лев'
		else:
			return 'Ваш знак зодиака: Дева'		
	elif month == 'сентябрь':
		if day < 22:
			return 'Ваш знак зодиака: Дева'
		else:
			return 'Ваш знак зодиака: Весы'
	elif month == 'октябрь':
		if day < 22:
			return 'Ваш знак зодиака: Весы'
		else:
			return 'Ваш знак зодиака: Скорпион'
	elif month == 'ноябрь':
		if day < 22:
			return 'Ваш знак зодиака: Скорпион'
		else:
			return 'Ваш знак зодиака: Стрелец'	
	elif month == 'декабрь':
		if day < 22:
			return 'Ваш знак зодиака: Стрелец'
		else:
			return 'Ваш знак зодиака: Козерог'	
	elif month == 'январь':
		if day < 22:
			return 'Ваш знак зодиака: Козерог'
		else:
			return 'Ваш знак зодиака: Водолей'	
	elif month == 'февраль':
		if day < 22:
			return 'Ваш знак зодиака: Водолей'
		else:
			return 'Ваш знак зодиака: Рыба'	


print(ex3())