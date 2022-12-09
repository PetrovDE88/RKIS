number1 = int(input('Значение первой переменной: '))
number2 = int(input('Значение второй переменной: '))
print('Первоначальные значения: {}, {}'.format(number1, number2))
number1, number2 = number2, number1
print('Поменяли местами: {}, {}'.format(number1, number2))
