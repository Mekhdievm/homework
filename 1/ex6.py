from math import sqrt

def ex6():
    
    print('Введите тип фигуры:')
    figure =  input()
    
    if figure == 'Круг':
        
        print('Введите радиус круга:')
        radius = int(input())
        return 3.1415 * radius ** 2;

    elif figure == 'Треугольник':

        print('Введите длину стороны A:')
        a = int(input())

        print('Введите длину стороны B:')
        b = int(input())

        print('Введите длину стороны C:')
        c = int(input())

        p = (a + b + c) / 2

        return sqrt(p * (p - a) * (p - b) * (p - c))

    elif figure == 'Прямоугольник':
        
        print('Введите длину стороны A:')
        a = int(input())

        print('Введите длину стороны B:')
        b = int(input())

        return a * b

print(ex6())