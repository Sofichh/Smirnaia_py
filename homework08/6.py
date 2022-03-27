line = input('Введите последовательность символов:')
maxlen = 0
k = 0
for i in range(len(line)):
    if line[i] == 's':
        k += 1
        if line[i+1] != 's':
            if k > maxlen:
                maxlen = k
            k = 0
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',  'о',
            'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
print(maxlen)
print('Зашиврованная буква:', alphabet[maxlen-1])
