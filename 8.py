n = int(input('Введите степень, до которой вы хотите вичсилить сумму ряда: '))
summ = 0
for i in range(0, n+1):
    summ += (-1)**i * (1/2)**i
print('Сумма ряда равна', summ)