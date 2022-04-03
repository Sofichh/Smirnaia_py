a = int(input('Введите начало отрезка: '))
b = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
for i in range(a, b+1, step):
    y = (i**3) + (2 * (i**2)) - (4 * i) + 1
    print("В точке", i, "функция равна", y)
