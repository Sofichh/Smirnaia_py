side = int(input('Введите длину стороны письма '))
n = 0
while side > 12:
    n = n + 2
    side = side/2
print('Письмо нужно сложить', n, 'раз')