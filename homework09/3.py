nuberofcells = int(input('Количество клеток: '))
cells = []
lst = []
for i in range(nuberofcells):
    effective = int(input('Введите эффективность клетки: '))
    cells.append(effective)
for k in range(nuberofcells):
    if cells[k] < k+1:
        lst.append(k+1)
print('Неподходящие клетки:', ' '.join(map(str, lst)))
