import random

mass = tuple((random.randint(0, 100) for _ in range(10)))  # Заполнение массива (списка) целыми случайными числами от 0 до 100

print('Массив:')
for elem in mass:
    print(elem, end=' ')
print()

print('Номер минимального элемента массива:', mass.index(min(mass))+1)
