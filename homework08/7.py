text = input('Введите текст: ')
lst = text.split(',')
max = len(lst[0])
for k in range(len(lst)-1):
    if max < len(lst[k+1]):
        max = len(lst[k+1])
print('Самое длинное слово, букв:', max)
