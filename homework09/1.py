num = int(input('Введите число: '))
nlst = []
for i in range(num//2):
    nlst.append(2*i+1)
if num % 2 != 0:
    nlst.append(num)
print('Список:', nlst)
