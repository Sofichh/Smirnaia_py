cost1 = int(input('Введите стоимость первого товара: '))
cost2 = int(input('Введите стоимость второго товара: '))
cost3 = int(input('Введите стоимость третьего товара: '))
summa = cost1 + cost2 + cost3
if summa > 10000:
    summa = summa*0.9
print('Итоговая сумма равна', summa)
