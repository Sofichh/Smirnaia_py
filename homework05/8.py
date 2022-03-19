summa = int(input('Вклад в банке составляет: '))
percent = int(input('Процент: '))
final_contribution = int(input('Желаемая сумма вклада: '))
years = 1
summa = summa*(1 + percent/100)
while summa < final_contribution:
    summa = summa * (1 + percent / 100)
    years = years + 1
print('Прежде чем сумма достигнет желаемого значения пройдет', years, 'лет.')
