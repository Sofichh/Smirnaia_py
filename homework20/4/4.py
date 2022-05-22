from work import Manager, Agent, Worker
sumsal = 0
lst = [Manager('Ivan', 'Vasnecov', 25), Manager('Marina', 'Tronina', 28), Manager('Levan', 'Ugliev', 23),
       Agent('Anika', 'Pipovna', 23, 90000), Agent('Taras', 'Pumpovich', 34, 100000),
       Agent('Tolya', 'Tolin', 56, 40000),
       Worker('Arseniy', 'Chuga', 19, 250), Worker('Nikola', 'Abramovich', 60, 100), Worker('', 'Chuga', 35, 160)]
k = 1
for i in lst:
    print(f'Заработная плата {k}-го служащего {i.salary()}')
    k += 1
    sumsal += i.salary()
print('Величина заработной платы всех служащих вместе', sumsal)
