k = 0
for i in (30, 31, 32, 33, 34, 35):
    print(i, '-й сектор', sep='')
    people = int(input('Людей в секторе: '))
    if people > 10:
        print('Нарушение! Слишком много людей в секторе!')
        k += 1
    else:
        print('Всё спокойно')
print('Количество нарушений:', k)
