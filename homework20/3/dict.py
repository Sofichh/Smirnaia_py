class MyDict:

    def __init__(self, dictt):
        self.dictt = dictt

    def get(self, key):
        return self.dictt.get(key, 0)

