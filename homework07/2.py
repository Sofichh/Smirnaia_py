n = int(input('Введите количество должников: '))
summ = 0
for i in range(0,n,5):
    print('Должник с номером', i)
    summ += int(input('Сколько должны? '))
print('Общая сумма долга:', summ)
