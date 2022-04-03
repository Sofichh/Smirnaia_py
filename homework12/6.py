dictionary = {1: ['Привет', 'Здравствуйте'], 2: ['Печально', 'Грустно'], 3: ['Весело', 'Радостно']}
word = input('Введите слово: ')
k = 0
for i in dictionary.values():
    for l in i:
        if word == l:
            k += 1
key1 = 0
if k == 0:
    print('Такого слова в словаре нет.')
else:
    for key, val in dictionary.items():
        for p in range(len(val)):
            if val[p] == word:
                key1 = key
    for k in range(len(dictionary[key])):
        if dictionary[key1][k] != word:
            print('Синоним:', dictionary[key1][k])
