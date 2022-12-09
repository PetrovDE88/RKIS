number = int(input('Введите число: '))

reverse_number = 0
copy_number = number
while copy_number > 0:
    reverse_number *= 10
    reverse_number += copy_number % 10
    copy_number //= 10

print(number == reverse_number)
