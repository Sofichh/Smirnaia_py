import math
volumeEarth = 10.8321*(10**11)
radius = float(input('Введите радиус случаной планеты: '))
volumeplanet = 4/3 * math.pi * pow(radius, 3)
ratio = volumeEarth/volumeplanet
if ratio > 1.0:
    print('Объем планеты Земля больше в', round(ratio, 3), 'раз')
else:
    print('Объем планеты Земля меньше в (1/', round(ratio, 3), ')=', round(1/round(ratio, 3), 3), ' раз', sep='')
