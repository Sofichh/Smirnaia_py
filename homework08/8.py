length = int(input('Введите длину колонтитула: '))
exclamation_point = int(input('Введите количество восклицательных знаков: '))
print('~'*((length-exclamation_point)//2), '!'*exclamation_point, '~'*((length-exclamation_point)//2), sep='')
