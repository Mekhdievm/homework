def ex2(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return 'Високосный год'
    else:
        return 'Обычный год'

print(ex2(2020))
print(ex2(2019))