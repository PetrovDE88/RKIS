number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))

print(
    'Первое число является делителем второго' if number1 and number2 and not (number2 % number1)
    else 'Первое число не является делителем второго'
)
