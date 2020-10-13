def ex3():
    day = int(input('Введите день: '))
    month = input('Введите месяц: ')
	
    if (month == 'март' and day < 22) or (month == 'февраль' and day > 22):
        return 'Ваш знак зодиака: Рыба'
    elif (month == 'апрель' and day < 22) or (month == 'март' and day > 22):
        return 'Ваш знак зодиака: Овен'
    elif (month == 'май' and day < 22) or (month == 'апрель' and day > 22):
        return 'Ваш знак зодиака: Телец'
    elif (month == 'июнь' and day < 22) or (month == 'май' and day > 22):
        return 'Ваш знак зодиака: Близнецы'
    elif (month == 'июль' and day < 22) or (month == 'июнь' and day > 22):
        return 'Ваш знак зодиака: Рак'
    elif (month == 'август' and day < 22) or (month == 'июль' and day > 22):
        return 'Ваш знак зодиака: Лев'
    elif (month == 'сентябрь' and day < 22) or (month == 'август' and day > 22):
        return 'Ваш знак зодиака: Дева'
    elif (month == 'октябрь' and day < 22) or (month == 'сентябрь' and day > 22):
        return 'Ваш знак зодиака: Весы'
    elif (month == 'ноябрь' and day < 22) or (month == 'октябрь' and day > 22):
        return 'Ваш знак зодиака: Скорпион'
    elif (month == 'декабрь' and day < 22) or (month == 'ноябрь' and day > 22):
        return 'Ваш знак зодиака: Стрелец'
    elif (month == 'январь' and day < 22) or (month == 'декабрь' and day > 22):
        return 'Ваш знак зодиака: Козерог'
    elif (month == 'февраль' and day < 22) or (month == 'январь' and day > 22):
        return 'Ваш знак зодиака: Водолей'

print(ex3())
