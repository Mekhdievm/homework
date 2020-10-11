def ex4(countries_temperature):
	for country in countries_temperature:
		print(country[0], ' - ',round(fah2cel(sum(country[1])/len(country[1])),1), 'С')
	return 1;

def fah2cel(fah):
    cel = 5.0*(fah - 32) / 9
    return cel

countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
ex4(countries_temperature)