import random


class Computer:

    def __init__(self):
        self.score = 0

    def taking(self, lstt, us):
        card = random.choice(lstt)
        lstt.remove(card)
        if ((self.score + card) > 21) and (card == 11):
            self.score += 1
        elif (self.score + card) >= 21:
            self.score += card
        else:
            self.score += card
        if self.score >= 21:
            us.stop(self.score)
        elif us.score >= 21:
            us.stop(self.score)


class User:

    def __init__(self, name):
        self.name = name
        self.score = 0

    def taking(self, lstt, comp):
        card = random.choice(lstt)
        lstt.remove(card)
        if ((self.score + card) > 21) and (card == 11):
            self.score += 1
        else:
            self.score += card

    def print_info(self):
        print(f'У вас столько очков: {self.score}')

    def stop(self, compsc):
        if (compsc > self.score):
            if compsc <= 21:
                print(f'Выиграл компьютер с счётом {compsc}. Вы потеряли потеряли столько очков: {self.score}')
            else:
                print(f'Вы выиграли с счётом {self.score}. Ваши очки увеличились на: {compsc}')
        elif (compsc < self.score):
            if self.score <= 21:
                print(f'Вы выиграли с счётом {self.score}. Ваши очки увеличились на: {compsc}')
            else:
                print(f'Выиграл компьютер с счётом {compsc}. Вы потеряли потеряли столько очков: {self.score}')
        else:
            print(f'Ничья, и вами было набрано: {self.score}, и компьютером : {compsc}')


class Cards:

    def __init__(self):
        self.two = 2
        self.three = 3
        self.four = 4
        self.five = 5
        self.six = 6
        self.seven = 7
        self.eight = 8
        self.nine = 9
        self.ten = 10
        self.jack = 10
        self.queen = 10
        self.king = 10
        self.ace = 11
