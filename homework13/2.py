import math
num = int(input('Введите количество чисел: '))
for i in range(num):
    number = float(input('Введите число: '))
    if number > 0:
        x = int(number) + 1
        print('x =', x, 'log(x) =', math.log(x))
    elif number < 0:
        x = int(number) - 1
        print('x =', x, 'exp(x) =', math.exp(x))
