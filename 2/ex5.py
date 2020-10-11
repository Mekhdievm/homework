def ex5(stream):
	stream_list = []
	for item in stream:
		stream_list.append(item.split(','))

	unique_list = []
	for item in stream_list:
		if item[1] not in unique_list:
			unique_list.append(item[1])

	print('Среднее количество просмотров на уникального пользователя:', round(sum([int(x[2]) for x in stream_list])/len(unique_list), 2))
	return 1

stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]
ex5(stream)
stream = [
    '2018-01-01,user100,150',
    '2018-01-07,user99,205',
    '2018-03-29,user1001,81'
]
ex5(stream)