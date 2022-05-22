import random


class Human:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.well_fed = 50

    def eating(self):
        self.well_fed += 10
        self.house.food -= 10

    def work(self):
        self.house.money += 300
        self.well_fed -= 15

    def play(self):
        self.well_fed -= 15

    def shop(self):
        self.house.food += 30

    def print_info(self):
        print(f'Имя жильца: {self.name}, Сытость: {self.well_fed}')


class Home:

    def __init__(self):
        self.money = 0
        self.food = 50

    def print_info(self):
        print(f'Еды в холодильнике - {self.food}, денег в тумбочке - {self.money}')


def life(hum, hom):
    num = random.randint(1, 6)
    if hum.well_fed < 20:
        hum.eating()
    elif hom.food < 10:
        hum.shop()
    elif hom.money < 50:
        hum.work()
    elif num == 1:
        hum.work()
    elif num == 2:
        hum.eating()
    else:
        hum.play()
