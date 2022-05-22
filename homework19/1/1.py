from warrior import Warrior
import random
first = Warrior('war1')
second = Warrior('war2')
warriors = [first, second]
while (first.health != 0) and (second.health != 0):
    defend = random.choice(warriors)
    for i in warriors:
        if defend != i:
            i.hit(defend)
            print(f'Атакующий: {i.name}, у соперника осталось {defend.health} очков здоровья\n')
            if defend.health == 0:
                print('Победу одержал:', i.name)

