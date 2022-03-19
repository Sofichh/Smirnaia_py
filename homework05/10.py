num = int(input('Загадайте число от 1 до 100: '))
i = 0
start = 1
guess = 50
end = 100
while i < 8:
    print('Предположительно это число', guess)
    question = int(input('Твое число равно, меньше или больше, чем это число? 1 - равно, 2 - больше, 3 - меньше. '))
    if question == 2:
        if guess == 99:
            guess = 100
            i = 8
        else:
            start = guess
            guess = guess + (end - start)//2
            i = i + 1
    elif question == 3:
        if guess == 2:
            guess = 1
            i = 8
        else:
            end = guess
            guess = guess - (end - start)//2
            i = i + 1
    else:
        i = 8
print('Загаданное число: ', guess)
