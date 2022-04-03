time = int(input('Время до обнуления: '))
for i in range(time, -1, -1):
    print('Секунд до взрыва', i)
    ques = input('Хотите обезвредить бомбу сейчас ')
    if ques == 'да':
        print('Бомба обезврежена')
        break
else:
    print('Бомба взорвалась')
