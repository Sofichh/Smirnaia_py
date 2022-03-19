num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
if (num3 == num2) & (num2 == num1):
    print(3)
elif (num3 == num2) or (num2 == num1) or (num3 == num1):
    print(2)
else:
    print(0)