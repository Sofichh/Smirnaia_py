rus_ex = int(input('Введите количество баллов по русскому языку: '))
math_ex = int(input('Введите количество баллов по математике: '))
inf_ex = int(input('Введите количество баллов по информатике: '))
if rus_ex + math_ex + inf_ex >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('Ты не поступил на бюджет(')