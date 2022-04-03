low = int(input('Нижняя граница: '))
high = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('Вывод:')
celsium = [k for k in range(low, high+1, step)]
if (high - low) % step != 0:
    celsium.append(high)
fahrenheit = [int(round(i * 1.8 + 32, 0)) if i >= 0 else int(round(i*1.8 - 32, 0)) for i in (celsium)]
print('C', '\t', 'F', '\t')
for i in range(len(celsium)):
    print(celsium[i], '\t', fahrenheit[i], '\t')
