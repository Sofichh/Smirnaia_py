line = input('Введите строку: ')
dict = {}
elements_odd_number = 0
for i in set(line):
    dict[i] = line.count(i)
for values in dict.values():
    if values % 2 != 0:
        elements_odd_number += 1
if elements_odd_number < 2:
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
