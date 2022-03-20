salary = [int(input('Введите зарплату: ')) for n in range(10)]
i = 0
err = 0
while i < 9:
    if salary[i] < salary[i+1]:
        i += 1
    else:
        i = 10
        err = 1
if err == 1:
    print('Зарплаты не упорядочены по возрастанию')
else:
    print('Зарплаты увеличиваются с каждым месяцем. Вы на своем месте!')

