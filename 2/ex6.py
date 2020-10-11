def ex6():
    print('Введите числа:')
    nums = input()
    nums_list = []
    nums_list = nums.split(' ')
    unique_list = []
    for num in nums_list:
        if num not in unique_list:
            unique_list.append(num)
    return ' '.join(unique_list)

print(ex6())