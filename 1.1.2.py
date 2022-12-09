dist1 = int(input('Введите расстояние в км.: '))
dist2 = int(input('Введите расстояние в метрах: '))

if dist1*1000 < dist2:
    result = str(dist1)+' км.'
elif dist1*1000 > dist2:
    result = str(dist2)+' м.'
else:
    result = 'равные расстояния'

print('Наименьшее:', result)
