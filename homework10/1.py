text = input('Введите текст: ')
lst = []
for i in range(len(text)):
    for k in ('а', 'о', 'у', 'е', 'ы', 'э', 'я', 'и', 'ю', 'ё'):
        if text[i] == k:
            lst.append(k)
print('Список гласных букв: ', lst)
print('Длина списка: ', len(lst))
