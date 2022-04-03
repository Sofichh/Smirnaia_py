number = int(input('Введите количество человек: '))
pedigree = {}
for i in range(number - 1):
    print(i+1, 'пара:', end=' ')
    child, parent = input().split()
    pedigree[child] = parent
result = {}
for name1 in pedigree.values():
    if name1 not in pedigree.keys():
        result[name1] = 0
for name2 in pedigree.keys():
    result[name2] = result[pedigree[name2]] + 1
print('“Высота” каждого члена семьи:')
for key in sorted(result):
    print(key, result[key])
