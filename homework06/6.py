n = int(input('Введите количество учащихся: '))
three = 0
four = 0
five = 0
lst_est = [int(input('Введите оценку ученика: ')) for i in range(n)]
for i in range(n):
    if lst_est[i] == 3:
        three += 1
    elif lst_est[i] == 4:
        four += 1
    else:
        five += 1
if (five > three) & (five > four):
    print('Сегодня больше отличников')
elif (four > three) & (four > five):
    print('Сегодня больше хорошистов')
else:
    print('Сегодня больше троечников')

