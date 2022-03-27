dayofweek = input('Введите день недели: ')
num = 1
coincident = 0
for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'):
    if coincident == 0:
        if dayofweek != day:
            num += 1
        else:
            coincident = 1
print('Номер дня недели:', num)

