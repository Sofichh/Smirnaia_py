mileage = int(input('Введите пробег: '))
date = int(input('Введите сегодняшнее число: '))
if mileage//100 + (mileage-mileage//100*100)//10 + mileage%10 > date:
    print('Сброс.')
    mileage = 0
    print('Пробег:', mileage)
else:
    print('Сегодня не сломался.')
    print('Пробег:', mileage)





