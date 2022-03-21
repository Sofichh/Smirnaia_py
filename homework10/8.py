n = int(input('Количество палок: '))
k = int(input('Количество бросков: '))
lst = [[int(input('Бросок. Сбиты палки с номера ')) if i == 0 else int(input('по номер ')) for i in range(2)] for _ in range(k)]
field = ['|' for i in range(n)]
for m in range(k):
    for i in range(lst[m][0]-1, lst[m][1]):
        field[i] = '.'
print('Результат:', ''.join(field))
