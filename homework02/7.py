velocity = int(input("Введите скорость в км\ч: "))
hours = int(input("Введите время в часах: "))
mark = velocity*hours
if mark > 114:
    mark = mark % 115
print('Номер километра, на котором  остановится Вася:', mark)
