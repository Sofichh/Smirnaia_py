lst = []
for i in range(10, 100):
    num = (i//10) * (i % 10) * 3
    if i == num:
        lst.append(i)
print('Замечательными числами являются:', ', '.join(map(str, lst)))