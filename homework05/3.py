account = int(input('Введите счет: '))
i = 1
number_of_signs = 0
while account//i != 0:
    number_of_signs = number_of_signs + 1
    i = i*10
print('Во вводимом числе', number_of_signs, 'десятичных чисел.')
