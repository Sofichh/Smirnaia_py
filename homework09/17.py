number_of_skates = int(input('Кол-во коньков: '))
skates = []
foot = []
amount = 0
for i in range(number_of_skates):
    print('Размер', i+1, 'пары:', end=' ')
    size = int(input())
    skates.append(size)
print('')
people = int(input('Кол-во людей: '))
for i in range(people):
    print('Размер ноги', i+1, 'человека:', end=' ')
    size_of_foot = int(input())
    foot.append(size_of_foot)
for _ in range(people):
    if max(foot) <= max(skates):
        amount += 1
        foot.remove(max(foot))
        skates.remove(max(skates))
    else:
        foot.remove(max(foot))
print('')
print('Наибольшее кол-во людей, которые могут взять ролики: ', amount)