line = input('Введите строку: ')
firsth = 0
for i in range(len(line)):
    if line[i] == 'h':
        if firsth == 0:
            firsth = 1
            stop = i - len(line)
        else:
            start = i - len(line) - 1
print(line[start:stop:-1])
