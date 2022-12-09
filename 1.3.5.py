def bytes_to_kbytes(number):
    return round(number / 1024, 5)


def kbytes_to_bytes(number):
    return number * 1024


number = int(input('Введите число: '))

print('''Что Вы хотите с ним сделать?
Введите 1, чтобы перевести его из байт в килобайты
Введите 2, чтобы перевести его из килобайт в байты''')
choice = 3
while choice < 1 or choice > 2:
    choice = int(input('Ваш выбор: '))

match choice:
    case 1:
        print('Число в килобайтах:', bytes_to_kbytes(number))
    case 2:
        print('Число в байтах:', kbytes_to_bytes(number))

