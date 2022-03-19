number = int(input('Введите шестизначный номер билета: '))
i = 100000
sum1 = 0
sum2 = 0
while i >= 1:
    if i > 100:
        sum1 = sum1 + number//i
        number = number % i
    else:
        sum2 = sum2 + number//i
        number = number % i
    i = i / 10
if sum1 == sum2:
    print('Билет счастливый!')
else:
    print('Билет обычный.')
