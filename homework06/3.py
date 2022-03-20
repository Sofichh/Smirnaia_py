summ = 0
for i in range(12):
    print(i+1, '-й месяц')
    sal = int(input('Введите зарплату: '))
    summ += sal
print('Средняя зарплата за год:', int(summ/12))
