class Parent:

    def __init__(self, name, age, lstchild):
        self.name = name
        self.age = age
        self.lstchild = lstchild

    def __str__(self):
        return self.name + ' ' + str(self.age) + '\n' + '\n'.join(
            [k.name + ' ' + str(k.age) + ' ' + k.stateofcalm + ' ' + k.stateofsatiety for k in self.lstchild])

    def info(self):
        print(f'Информация о родителе с именем {self.name}:', end=' ')
        infor = input()
        return infor

    def canitbechild(self, k):
        if self.age - k.age < 16:
            self.lstchild.remove(k)
            return f'{k.name} не может быть ребенком родителя с именем {self.name}'
        else:
            return f'{k.name} может быть ребенком родителя с именем {self.name}'

    def calm(self):
        for i in self.lstchild:
            if i.stateofcalm in ['crying', 'screaming', 'capricious', 'scared', 'hooligans']:
                i.stateofcalm = 'calm'
                return f'Ребенок с именем {i.name} спокоен'

    def eating(self):
        for i in self.lstchild:
            if i.stateofsatiety == 'hungry':
                i.stateofsatiety = 'well - fed'
                return f'Ребенок с именем {i.name} сыт'


class Child:

    def __init__(self, name, age, stateofcalm, stateofsatiety):
        self.name = name
        self.age = age
        self.stateofcalm = stateofcalm
        self.stateofsatiety = stateofsatiety
