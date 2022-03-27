message = input('Введите сообщение: ')
words = message.split()
position = 1
for i in range(len(words)):
    for k in range(len(words[i])):
        if words[i][k] != '*':
            position += 1
        else:
            fixposition = position
print('Символ ‘*’ стоит на позиции', fixposition)
