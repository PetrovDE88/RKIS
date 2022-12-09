from random import randint

mass = tuple(tuple(tuple(randint(0, 20) for _ in range(5)) for _ in range(5)) for _ in range(5))
print(mass)
count = 0
print('Индексы первого вхождения минимальных элементов массива:')
for num_i, i in enumerate(mass):
    for num_j, j in enumerate(i):
        print(f'{num_i}, {num_j}, {j.index(min(j))}')
        count += 1
