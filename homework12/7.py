number = int(input('Введите кол-во заказов: '))
dictionary = {}
for i in range(number):
    print(i+1, 'заказ: ', end=' ' )
    order = input('')
    name = order.split()[0]
    pizza = order.split()[1]
    num = int(order.split()[2])
    if name not in dictionary:
        dictionary[name] = {pizza: num}
    else:
        if pizza not in dictionary[name]:
            dictionary[name] |= {pizza: num}
        else:
            dictionary[name][pizza] += num
print(dictionary)
for sur, elem in sorted(dictionary.items()):
    print(sur, ':', sep='')
    for name_pizza in elem.keys():
        print('  ', name_pizza, ': ', elem[name_pizza], sep='')

