def ex1(word):
    lenght = len(word)
    if (lenght % 2) == 0 :
        middle = int(lenght/2)
        return word[middle-1:middle+1]
    else :
        middle = int(lenght/2)
        return word[middle]

word = 'test'
print(ex1(word))
word = 'testing'
print(ex1(word))