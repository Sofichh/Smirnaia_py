import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square(self):
        s = math.pi * self.r ** 2
        return round(s, 2)

    def perimetr(self):
        p = 2 * math.pi * self.r
        return round(p, 2)

    def increase(self, koeff):
        self.r *= koeff

    def intersection(self, x2, y2, r2):
        if (self.x != x2) or (self.y != y2):
            if (self.x - x2) ** 2 + (self.y - y2) ** 2 > (self.r + r2) ** 2:
                return 'Нет, окружности не пересекаются'
            else:
                return 'Да, окружности пересекаются'
        else:
            if self.r != r2:
                return 'Нет, окружности не пересекаются'
            else:
                return 'Oкружности совпадают'

