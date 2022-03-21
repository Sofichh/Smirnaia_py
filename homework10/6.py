n = int(input('Введите количество элементов списка: '))
lst = [int(input('Введите элемент списка:')) for k in range(n)]
for k in range(n):
    if lst[k] == 0:
        lst.append(lst.pop(k))
stop = n - lst.count(0)
print(lst[0:stop])
