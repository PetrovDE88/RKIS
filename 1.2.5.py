print('Сумма всех целых чисел от 100 до 500 включительно:', sum(i for i in range(100, 501)))
number = 500
while number >= 500:
    number = int(input('Введите число < 500: '))
print(f'Сумма всех целых чисел от {number} до 500 включительно:', sum(i for i in range(number, 501)))
