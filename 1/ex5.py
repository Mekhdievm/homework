def ex5(ticket):

	first = int(ticket[0])+int(ticket[1])+int(ticket[2])
	last  = int(ticket[3])+int(ticket[4])+int(ticket[5])
	if first == last:
	 	return 'Счастливый билет'
	else:
		return 'Несчастливый билет'


print(ex5('123456'))
print(ex5('123321'))