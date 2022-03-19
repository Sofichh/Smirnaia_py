hours = int(input('Введите отработанные часы: '))
credit = int(input('Введите остаток по кредиту: '))
meal = int(input('Введите траты на еду: '))
if ((200*hours)/2**3 + hours) >= credit + meal:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')


