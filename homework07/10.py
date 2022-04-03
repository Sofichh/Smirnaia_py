boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))
answer = ''
if (boys > 2 * girls) or (girls > 2 * boys):
    print('Нет решения.')
elif boys >= girls:
    i = boys - girls
    for _ in range(i):
        answer += 'BGB'
    for __ in range(girls - i):
        answer += 'BG'
else:
    i = girls - boys
    for _ in range(i):
        answer += 'GBG'
    for __ in range(boys - i):
        answer += 'GB'
print(answer)
