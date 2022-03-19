square = int(input('Введите площадь квартиры в кв.м.: '))
cost = int(input('Введите стоимость в млн.: '))
if (square >= 100) & (cost <= 10):
    print('Подходит')
elif (square >= 80) & (cost <= 7):
    print('Подходит')
else:
    print('Не подходит')