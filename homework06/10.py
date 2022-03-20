n = int(input('Введите количество карт в колоде: '))
lst = [i+1 for i in range(n)]
lst1 = [int(input('Введите номер оставшейся карты: ')) for i in range(n-1)]
err = 0
k = 0
num = 0
while k < n-1:
    if lst[k] == lst1[k]:
        k += 1
        num = k + 1
    else:
        num = k + 1
        k = n
        err = 1
print('Потерялась карточка под номером: ', num)
