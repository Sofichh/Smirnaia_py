educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
summa = expenses
for i in range(1, 11):
    expenses = expenses * 1.03
    summa += expenses
summa = summa - 12 * educational_grant
print('У родителей нужно попросить ',summa)

