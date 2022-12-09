from random import randint


def calculate(mass: tuple):
    positive = 0
    negative = 0
    zero = 0
    for elem in mass:
        if elem > 0:
            positive += 1
        elif elem < 0:
            negative += 1
        else:
            zero += 1
    return positive, negative, zero


numbers = tuple(randint(-100, 100) for _ in range(25))

print('Массив:')
print(numbers)
pos, neg, zero = calculate(numbers)
print('''Положительных элементов: {}
Отрицательных элементов: {}
Нулей: {}'''.format(pos, neg, zero))
