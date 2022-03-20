n = int(input('Введите число: '))
fact = 1
for i in range(n+1):
    if i == 0:
        fact = 1
    else:
        fact *= i
print('Факториал числа', n, 'равен', fact)