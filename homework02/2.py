first_quarter = int(input("Введите доход за первый квартал года: "))
second_quarter = int(input("Введите доход за второй квартал года: "))
penultimate_quarter = int(input("Введите доход за предпоследний квартал года: "))
last_quarter =int(input("Введите доход за последний квартал года: "))
sum1 = first_quarter + second_quarter
sum2 = penultimate_quarter + last_quarter
fraction = sum1/sum2
print(fraction)