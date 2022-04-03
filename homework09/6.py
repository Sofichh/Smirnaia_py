word = input('Введите слово: ')
k = 0
for i in range(len(word)):
    if word.count(word[i]) == 1:
        k += 1
print('Количество уникальных букв:', k)
