class Person:

    def __init__(self, __name, __surname, __age):
        self.__name = __name
        self.__surname = __surname
        self.__age = __age


class Employee(Person):

    def salary(self):
        pass


class Manager(Employee):

    def __init__(self, __name, __surname, __age):
        super().__init__(__name, __surname, __age)

    def salary(self):
        return 13000


class Agent(Employee):

    def __init__(self, __name, __surname, __age, volumesale):
        self.volumesale = volumesale
        super().__init__(__name, __surname, __age)

    def salary(self):
        return 5000 + 0.5 * self.volumesale


class Worker(Employee):

    def __init__(self, __name, __surname, __age, hours):
        self.hours = hours
        super().__init__(__name, __surname, __age)

    def salary(self):
        return 100 * self.hours