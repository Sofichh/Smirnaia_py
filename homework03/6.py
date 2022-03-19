konstantin = int(input('Кубик Кости: '))
owner = int(input('Кубик владельца: '))
if konstantin >= owner:
    print('Разность', konstantin - owner)
    print('Платит Костя')
else:
    print('Сумма', konstantin + owner)
    print('Платит владелец')
print('Игра окончена!')
