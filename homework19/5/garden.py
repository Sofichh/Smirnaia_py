class Gardener:

    def __init__(self, name, veg):
        self.name = name
        self.veg = veg

    def care(self):
        p = 0
        self.veg.lst = [k + 1 if k < 4 else k for k in self.veg.lst]
        for g in self.veg.lst:
            if g == 5:
                p = 1

        if p:
            ans = input('Хотите ли вы еще посадить картошку? ').lower()
            if ans == 'да':
                self.veg.lst = [1 if k == 5 else k for k in self.veg.lst]
        return self.veg.lst

    def harvesting(self):
        harvest = 0
        for n in self.veg.lst:
            if n == 4:
                harvest += 1
        self.veg.lst = [5 if k == 4 else k for k in self.veg.lst]
        print('Урожай:', harvest)
        print('Грядка после сбора урожая:', self.veg.lst)
        return harvest


class Gardenbed:

    def __init__(self, lst):
        self.lst = lst

