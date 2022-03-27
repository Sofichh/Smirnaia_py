x = 8
y = 10
while (0 <= x <= 15) & (0 <= y <= 20):
    print('Марсоход находится на позиции ', x, ', ', y, sep='')
    if (x == 0) or (x == 15) or (y == 0) or (y == 20):
        print('Необходимо обратить внимание на границы.')
    order = input('Введите команду:')
    if order == 'W':
        y += 1
    elif order == 'S':
        y -= 1
    elif order == 'A':
        x -= 1
    elif order == 'D':
        x += 1
