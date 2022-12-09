from random import randint

mass = tuple(tuple(randint(0, 9) for _ in range(5)) for _ in range(5))
mass2 = list(list())
for string in mass:
    print(string)

for i in range(len(mass)-1):
    for j in range(len(mass)):
        mass2.append(max(mass[i][j], mass[i+1][j]))

print('Список из максимальных рядом стоящих по вертикали элементов:', mass2)
