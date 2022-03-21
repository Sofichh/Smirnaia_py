import random
lst1 = [float('{:.2f}'.format(random.uniform(5, 10))) for k in range(20)]
lst2 = [float('{:.2f}'.format(random.uniform(5, 10))) for k in range(20)]
lst3 = []
for k in range(20):
    if lst1[k] > lst2[k]:
        lst3.append(float('{:.2f}'.format(lst1[k])))
    else:
        lst3.append(float('{:.2f}'.format(lst2[k])))
print('Первая команда:', lst1)
print('Вторая команда:', lst2)
print('Победители тура:', lst3)
