n = int(input('Введите максимальное число: '))
line = ''
dictionary = {'Да': [], 'Нет': []}
answer = ''
while True:
    print()
    line = input('Нужное число есть среди вот этих чисел: ')
    lst = line.split()
    if line == 'Помогите!':
        print()
        break
    answer = input('Ответ Артёма: ')
    dictionary[answer].extend(lst)
for i in dictionary['Нет']:
    if dictionary['Да'].count(i) >= 1:
        dictionary['Да'].remove(i)
print('Артём мог загадать следующие числа:', ' '.join(dictionary['Да']))
