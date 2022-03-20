sequence = '114 12 14 10605 4907 450'
numbers = sequence.split()
for i in range(len(numbers)):
    if (int(numbers[i]) % 2 == 0) & (int(numbers[i]) % 3 != 0):
        print('Число', numbers[i], 'подходит')
    else:
        print('Число', numbers[i], 'не подходит')
