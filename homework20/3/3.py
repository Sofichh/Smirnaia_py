from  dict import MyDict
dict1 = dict(звезды=['Солнце', 'Альтаир', 'Альдебаран', 'Денеб'],
             планеты=['Земля', 'Марс', 'Венера', 'Юпитер', 'Сатурн'])
diction = MyDict(dict1)
print(diction.get('спутники'))
print(diction.get('планеты'))
