print('Начался 8-часовой рабочий день')
i = 1
tasks = 0
calls = 0
while i <= 8:
    print(i, '-й час', sep='')
    task = int(input('Сколько задач решит Максим? '))
    tasks = tasks + task
    call = int(input('Звонит жена. Взять трубку? (1 - да, 0 - нет): '))
    if call == 1:
        calls = calls + 1
    i = i + 1
print('Рабочий день закончился. Всего выполнено задач: ', tasks)
if calls > 0:
    print('Нужно зайти в магазин.')
