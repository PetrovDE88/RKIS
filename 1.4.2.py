from random import randint


def completion(start, stop):
    if start > stop:
        return tuple(randint(stop, start) for _ in range(stop, start))
    else:
        return tuple(randint(start, stop) for _ in range(start, stop))


num1 = int(input('Введите начало диапазона: '))
num2 = int(input('Введите конец диапазона: '))

result = completion(num1, num2)
print('Количество элементов массива:', len(result))
print('Массив:')
print(result)
