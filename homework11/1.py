line = input('Доступное меню: ')
lst = line.split(';')
menu = ', '.join(lst)
print('На данный момент в меню есть:', menu)
