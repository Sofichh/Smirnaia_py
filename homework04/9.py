income = int(input('Введите свой доход: '))
if income > 50000:
    tax = 0.3 * (income - 50000) + 0.2 * 40000 + 0.13 * 10000
elif (income > 10000) & (income < 50000):
    tax = 0.2 * (income - 10000) + 0.13 * 10000
else:
    tax = 0.13 * income
print('Сумма налога:', tax)
