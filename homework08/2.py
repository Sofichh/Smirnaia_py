words = []
k = 0
for i in range(10):
    f = input('Введите слово: ')
    words.append(f)
for word in words:
    if word == 'Карамба':
        k += 1
print('На борт попали', k, 'человек')