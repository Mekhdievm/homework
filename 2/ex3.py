def ex3(boys, girls):
	if len(boys) != len(girls):
		print('Внимание, кто-то может остаться без пары!')
		return 0
	
	boys = sorted(boys)
	girls = sorted(girls)
	print('Идеальные пары:') 
	i = 0
	while i < len(girls):
		print(boys[i], ' и ', girls[i])
		i+=1
	return 1


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
ex3(boys, girls)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
ex3(boys, girls)