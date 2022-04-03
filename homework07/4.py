a = int(input('Число а: '))
b = int(input('Число b: '))
c = int(input('Числа должны быть кратны '))
summ = 0
n = 0
for i in range(a, b+1, 1):
    if (i % c == 0) & (i != 0):
        summ += i
        n += 1
print('Среднее арифметическое:', summ/n)

