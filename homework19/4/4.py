from classes import Parent, Child
firstparent = Parent('Elens', 32, [Child('Miron', 5, 'calm', 'hungry'), Child('Agata', 10, 'crying', 'well - fed'),
                                   Child('Konstantin', 28, 'quiet', 'well - fed')])
print(firstparent.__str__())
firstparent.info()
for i in firstparent.lstchild:
    print(firstparent.canitbechild(i))
print(firstparent.calm())
print(firstparent.eating())
print(firstparent.__str__())

print('Все дети сыты и спокойны. Родитель молодец!')
