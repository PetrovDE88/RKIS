number = int(input('Введите число: '))
reverse_number = 0
while number > 0:
    reverse_number *= 10
    reverse_number += number % 10
    number //= 10

print(reverse_number)