lst = []
k = 0
for i in range(10):
    num = int(input('Введите число: '))
    lst.append(num)
    if (num % 2 == 0) & (num > 0):
        k += 1
print('Среди чисел', ', '.join(map(str, lst)), 'одновременно четными и положительными являются', k)
