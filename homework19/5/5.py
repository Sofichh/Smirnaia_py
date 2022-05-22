from garden import Gardener, Gardenbed
print('1 - картофель посажен, 2 - росток, 3 - маленькая, 4 - зрелая, 5 - пустая лунка')
harv = 0
potato = Gardenbed([1, 2, 1, 1, 2])
gardener = Gardener('Ivan Petrovich', potato)
# while potato.lst != ['_','_','_','_','_']:
while potato.lst != [5, 5, 5, 5, 5]:
    print('Грядка после ухода:', gardener.care())
    harv += gardener.harvesting()
print('Сезон окончен, урожай составил', harv, 'картофелин')
