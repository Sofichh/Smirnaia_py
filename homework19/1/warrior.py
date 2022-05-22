class Warrior:

    def __init__(self, name, health=100):
        self.health = health
        self.name = name

    def hit(self, obj):
        obj.health -= 20