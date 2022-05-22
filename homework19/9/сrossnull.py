class Cross:

    def cross(self, field):
        strr = int(input('В какой строке хотите поставиь крестик?(напишите число) '))
        colomn = int(input('В каком столбце?(напишите число) '))
        if strr == 1:
            field.first[colomn - 1] = 1
        if strr == 2:
            field.second[colomn - 1] = 1
        if strr == 3:
            field.third[colomn - 1] = 1
        field.show()


class Null:

    def null(self, field):
        strr = int(input('В какой строке хотите поставиь нолик?(напишите число) '))
        colomn = int(input('В каком столбце?(напишите число) '))
        if strr == 1:
            field.first[colomn - 1] = 0
        if strr == 2:
            field.second[colomn - 1] = 0
        if strr == 3:
            field.third[colomn - 1] = 0
        field.show()


class Field:

    def __init__(self):
        self.first = ['_', '_', '_']
        self.second = ['_', '_', '_']
        self.third = ['_', '_', '_']

    def show(self):
        print(self.first, self.second, self.third, sep='\n')

    def check(self):
        for k in self.first, self.second, self.third:
            if '_' not in k:
                if sum(k) == 3:
                    print('Выиграл игрок с крестиками')
                    return 1
                elif sum(k) == 0:
                    print('Выиграл игрок с ноликами')
                    return 1
        for l in 0, 1, 2:
            lst = [self.first[l], self.second[l], self.third[l]]
            if '_' not in lst:
                if sum(lst) == 3:
                    print('Выиграл игрок с крестиками')
                    return 1
                elif sum(lst) == 0:
                    print('Выиграл игрок с ноликами')
                    return 1
        if self.second[1] == 1:
            if (self.first[0] == 1) and (self.third[2] == 1):
                print('Выиграл игрок с крестиками')
                return 1
            elif (self.first[2] == 1) and (self.third[0] == 1):
                print('Выиграл игрок с крестиками')
                return 1
        if self.second[1] == 0:
            if (self.first[2] == 0) and (self.third[0] == 0):
                print('Выиграл игрок с ноликами')
                return 1
            elif (self.first[0] == 0) and (self.third[2] == 0):
                print('Выиграл игрок с ноликами')
                return 1
        return 0

