def ex4(width, length, height):
	
	if (width < 15) and (length < 15) and (height < 15):
		return "Коробка №1"	
	elif (width > 15 and width < 50) or (length > 15 and length < 50) or (height > 15 and height < 50) :
		return "Коробка №2"
	elif length > 200:
		return "Упаковка для лыж"
	else:
		return "Стандартная коробка №3"

print(ex4(10,205,5))