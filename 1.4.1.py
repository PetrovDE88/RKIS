number = int(input('Введите натуральное число: '))

summ = 0
product = 1
while number != 0:
    summ += number % 10
    product *= number % 10
    number = number // 10

print('Сумма цифр числа:', summ)
print('Произведение цифр числа:', product)
