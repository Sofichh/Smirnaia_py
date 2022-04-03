number = int(input('Кол-во чисел: '))
lst = [int(input('Число: ')) for i in range(number)]
print('Последовательность:', ' '.join(map(str, lst)))
lst1 = lst
i = 0
while lst1 != lst1[::-1]:
        i += 1
        lst1 = lst[i:]
lst1 = []
symmetry_number = i
k = 0
while symmetry_number > 0:
    lst1.append(lst[symmetry_number-1])
    symmetry_number -= 1
    k += 1
print('Нужно приписать чисел:', k)
print('Сами числа:', ' '.join(map(str, lst1)))