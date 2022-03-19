total = int(input('Введите количество опыта: '))
if total < 1000:
    print('Ваш уровень: 1')
elif total < 2500:
    print('Ваш уровень: 2')
elif total < 5000:
    print('Ваш уровень: 3')
else:
    print('Ваш уровень: 4')
