from circle import Circle

x1, y1, r1 = map(int, input('Введите координаты х, у и радиус первой окружности через пробел ').split())
print(x1, y1, r1, sep=',')
C1 = Circle(x1, y1, r1)
print('Периметр окружности:', C1.perimetr())
print('Площадь внутри окружности:', C1.square())
incrcoeff = int(input('Во сколько раз хотите увеличить окружность? '))
C1.increase(incrcoeff)
print(f'Радиус после увеличения в {incrcoeff} раз(а) :', C1.r)
x2, y2, r2 = map(int, input('Введите координаты х, у и радиус второй окружности через пробел ').split())
print(C1.intersection(2, 4, 5))