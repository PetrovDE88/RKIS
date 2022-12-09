def search(target):
    if target in mass:
        return mass.index(target)
    elif target < mass[0]:
        return 0
    elif target > mass[len(mass) - 1]:
        return len(mass)
    else:
        for i in range(len(mass) - 1):
            if mass[i] < target and mass[i + 1] > target:
                return i + 1


mass = (1, 3, 5, 6)
target = 3
target2 = 4
print('Место в массиве:', search(target))
print('Место в массиве:', search(target2))
