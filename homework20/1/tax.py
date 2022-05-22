class Property:

    def __init__(self):
        self.worth = worth

    def tax(self):
        return None


class Apartment(Property):

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        tax = self.worth / 1000
        return tax


class Car(Property):

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        tax = self.worth / 200
        return tax


class CountryHouse(Property):

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        tax = self.worth / 500
        return tax
