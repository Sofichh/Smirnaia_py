import random
from life2 import People, House, Husband, Wife, Child, Cat
income = 0
furcoat = 0
food = 0
cat1 = Cat('Murzik')
cat2 = Cat('Masya')
husband = Husband('Yurij')
wife = Wife('Kristina')
child = Child('Kira')
home = House()
for n in range(365):
    home.dirt += 5
    for k in husband, wife, child:
        if home.dirt > 90:
            k.happiness -= 10
        if k.well_feed < 20:
            food += k.eating(home)
        elif (k == wife) and (home.food < 55):
            k.shop(home)
        elif (home.money < 130) and (k == husband):
            income += k.work(home)
        elif (home.dirt > 80) and (k == wife):
            k.cleanup(home)
        elif (k.happiness <= 20):
            r = random.randint(1, 2)
            if r == 1:
                cat = random.choice(cat1, cat2)
                k.pettingcat(cat)
            else:
                if k == wife:
                    if home.money > 3500:
                        k.furcoat += k.buyfurcoat(home)
                    else:
                        cat = random.choice(cat1, cat2)
                        k.pettingcat(cat)
                if k == husband:
                    husband.play()
                if k == child:
                    child.play()
        else:
            r = random.randint(1, 2)
            if r == 1:
                if k == wife:
                    k.cleanup(home)
                if k == husband:
                    income += k.work(home)
                if k == child:
                    k.sleep()
            else:
                cat = random.choice([cat1, cat2])
                if k == wife:
                    if home.money > 3500:
                        furcoat += k.buyfurcoat(home)
                    else:
                        k.pettingcat(cat)
                if k == husband:
                    random.choice([k.play(), k.pettingcat(cat)])
                if k == child:
                    random.choice([k.play(), k.pettingcat(cat)])
    for h in cat1, cat2:
        if h.well_feed < 10:
            food += h.eating(home)
        else:
            r = random.randint(1, 2)
            if r == 1:
                h.sleep()
            else:
                h.tearwallpaper(home)
for k in husband, wife, child:
    print(f'Жилец: {k.name}, сытость: {k.well_feed}, состояние счастья: {k.happiness}', sep=' ')
    if (k.well_feed < 0) or (k.happiness < 10):
        print('и он мертв((')
for n in cat1, cat2:
    print(f'Питомец: {n.name}, сытость: {n.well_feed}', sep=' ')
    if n.well_feed < 0:
        print('и он мертв((')
print(f'Итоги года: денег заработано - {income}, съедено еды - {food}, куплено шуб - {furcoat}')
