import math


class Car:

    def __init__(self, x, y, angl):
        self.x = x
        self.y = y
        self.angl = angl

    def move(self, dist):
        self.x = dist * math.cos(self.angl)
        self.y = dist * math.sin(self.angl)

    def turn(self, rot):
        self.angl += rot


class Bus(Car):

    def __init__(self, x, y, angl, passenger):
        super().__init__(x, y, angl)
        self.passenger = passenger
        self.money = 0

    def enter(self, numpasent):
        self.passenger += numpasent
        return numpasent

    def exit(self, numpas):
        self.passenger -= numpas

    def move(self, dist, numpasent):
        self.x = dist * math.cos(self.angl)
        self.y = dist * math.sin(self.angl)
        self.money += numpasent * 50
        return numpasent

