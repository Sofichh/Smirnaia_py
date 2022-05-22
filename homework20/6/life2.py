class Cat:

    def __init__(self, name):
        self.well_feed = 30
        self.name = name

    def sleep(self):
        self.well_feed -= 10

    def tearwallpaper(self, home):
        self.well_feed -= 10
        home.dirt += 5

    def eating(self, home):
        home.cfood -= 10
        self.well_feed += 20
        return 10


class People:

    def __init__(self, name):
        self.well_feed = 30
        self.happiness = 100
        self.name = name

    def eating(self, home):
        pass

    def pettingcat(self, cat):
        self.well_feed -= 10
        self.happiness += 5


class Husband(People):

    def __init__(self, name):
        super().__init__(name)

    def eating(self, home):
        home.food -= 30
        self.well_feed += 30
        return 30

    def play(self):
        self.well_feed -= 10
        self.happiness += 20

    def work(self, home):
        self.well_feed -= 10
        home.money += 150
        return 150


class Wife(People):

    def __init__(self, name):
        super().__init__(name)

    def eating(self, home):
        home.food -= 30
        self.well_feed += 30
        return 30

    def shop(self, home):
        home.food += 300
        home.cfood += 80
        home.money -= 380
        self.well_feed -= 10

    def buyfurcoat(self, home):
        home.money -= 350
        self.happiness += 60
        self.well_feed -= 10
        return 1

    def cleanup(self, home):
        self.well_feed -= 10
        home.dirt -= 100


class Child(People):

    def __init__(self, name):
        super().__init__(name)

    def eating(self, home):
        home.food -= 20
        self.well_feed += 20
        return 15

    def play(self):
        self.well_feed -= 10
        self.happiness += 20

    def sleep(self):
        self.well_feed -= 10


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cfood = 30
        self.dirt = 0

