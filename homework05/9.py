hidden_number = 7
number = int(input('Введите число: '))
i = 1
while number != hidden_number:
    if number < hidden_number:
        print('Число меньше, чем нужно. Попробуйте еще раз!')
    else:
        print('Число больше, чем нужно. Попробуйте еще раз!')
    number = int(input('Введите число: '))
    i = i + 1
print('Вы угадали! Число попыток:', i)

