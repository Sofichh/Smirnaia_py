x = int(input('Введите чило х: '))
nominator = 1
denominator = 1
for i in range(1, 6):
    nominator *= x - (2**i-1)
    denominator *= x - 2**i
res = nominator/denominator
print('Вычет равен', res)
