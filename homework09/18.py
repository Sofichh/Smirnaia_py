people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', number, 'человек')
circle = [i + 1 for i in range(people)]
out = 0
for _ in range(people - 1):
    print('Текущий круг людей', circle)
    start = out % len(circle)
    out = (start + number - 1) % len(circle)
    print('Начало счёта с номера', circle[start])
    print('Выбывает человек под номером', circle[out])
    circle.remove(circle[out])
    print()
print('Остался человек под номером', circle.pop())
