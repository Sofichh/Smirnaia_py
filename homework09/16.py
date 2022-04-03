firstlst = []
secondlst = []
for i in range(3):
    firstlst.append(int(input('Введите элемент первого списка: ')))
for i in range(7):
    secondlst.append(int(input('Введите элемент второго списка: ')))
firstlst = firstlst + secondlst
firstlst = list(set(firstlst))
print('Новый первый список с уникальными элементами:', firstlst)
