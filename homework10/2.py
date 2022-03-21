n = int(input('Введите длину списка: '))
lst = []
for k in range(n):
    if k % 2 == 0:
        lst.append(1)
    else:
        lst.append(k % 5)
print('Результат:', lst)
