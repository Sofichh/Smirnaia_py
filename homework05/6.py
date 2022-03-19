grade = int(input('Введите число: '))
positive = 0
negative = 0
while grade != 0:
    if grade > 0:
        positive = positive + 1
    else:
        negative = negative + 1
    grade = int(input('Введите число: '))
print('Количество положительных чисел:', positive)
print('Количество отрицательных чисел:', negative)



