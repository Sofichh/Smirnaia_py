friends = int(input('Кол-во друзей: '))
number = int(input('Долговых расписок: '))
lst = [0 for _ in range(friends)]
for i in range(number):
    print(i + 1, 'расписка')
    index1 = int(input('Кому: '))
    index2 = int(input('От кого: '))
    summ = int(input('Сколько: '))
    lst[index1-1] -= summ
    lst[index2-1] += summ
print()
for i in range(friends):
    print('Баланс друзей:')
    print(i+1, ':', lst[i])

