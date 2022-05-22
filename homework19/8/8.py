import random
from game import Cards, Computer, User
spades = Cards()
hearts = Cards()
clubs = Cards()
diamonds = Cards()
user1 = User('sonic')
comput = Computer()
lst = []
for n in spades, hearts, clubs, diamonds:
    for k in n.two, n.three, n.four, n.five, n.six, n.seven, n.eight, n.nine, n.ten, n.jack, n.queen, n.king, n.ace:
        lst.append(k)
user1.taking(lst, comput)
user1.taking(lst, comput)
comput.taking(lst, user1)
comput.taking(lst, user1)
user1.print_info()
while (comput.score < 21) and (user1.score < 21):
    answ = input('Хотите взять карту? ').lower()
    if answ == 'да':
        user1.taking(lst, comput)
        user1.print_info()
        comput.taking(lst, user1)
    else:
        random.choice([comput.taking(lst, user1), print('Компьютер тоже не взял карту')])
        user1.stop(comput.score)
        break
        