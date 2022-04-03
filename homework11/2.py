line = input('Введите строку: ')
lst = line.split()
max = lst[0]
for k in range(len(lst)-1):
    if len(max) < len(lst[k+1]):
        max = lst[k+1]
print('Самое длинное слово:', max)
print('Его длина равна', len(max))
