number = int(input('Количество видеокарт: '))
lst =[]
max = 0
for i in range(number):
    model = int(input('Видеокарта: '))
    lst.append(model)
for i in lst:
    if max < i:
        max = i
print('Стары список видеокарт:', lst)
lst.pop(lst.index(max))
print('Новы список видеокарт:', lst)
