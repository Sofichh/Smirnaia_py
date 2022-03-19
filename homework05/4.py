amount_of_days = int(input('Введите количество дней в месяце: '))
number_of_months = 0
while amount_of_days != 0:
    if (amount_of_days % 2) == 0:
        number_of_months = number_of_months + 1
    amount_of_days = int(input('Введите количество дней в месяце: '))
print('Количество месяцев с четным количеством дней: ', number_of_months)
