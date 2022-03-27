row = int(input('Введите количество рядов: '))
seats = int(input('Введите количество сидений в ряде: '))
meters = int(input('Введите количество метров между рядами: '))
print('')
print('СЦЕНА')
print('')
for i in range(row):
    print('=' * seats, '*' * meters, '=' * seats)