from students import Students


def nom(a):
    return a.av_score()


lst = [Students('Ivanov Ivan', 3, [4, 5, 5, 4, 5]), Students('Borisov Boris', 2, [5, 5, 5, 4, 5]),
       Students('Antonov Anton', 1, [4, 5, 3, 4, 3]),
       Students('Petrova Irina', 1, [5, 5, 5, 5, 5]), Students('Danilova Darina', 3, [4, 4, 5, 4, 5]),
       Students('Vladlenov Vlad', 2, [4, 5, 5, 3, 3]),
       Students('Nuriev Roman', 1, [5, 5, 5, 3, 5]), Students('Kuznezov Arsenij', 2, [5, 5, 5, 5, 5]),
       Students('Arkova Anna', 1, [3, 5, 4, 4, 5]),
       Students('Mashkova Oksana', 3, [5, 5, 5, 5, 5])]
lst.sort(key=nom)
lstt = []
for i in lst:
    lstt.append(i.surnamename)
print(lstt)
