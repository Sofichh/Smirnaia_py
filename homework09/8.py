num_list = [1, 2, 3, 4, 5]
print('Изначальный список:', num_list)
k = int(input('Введите сдвиг: '))
for i in range(k):
    num_list.insert(0, num_list.pop())
print('Сдвинутый список: ', num_list)
