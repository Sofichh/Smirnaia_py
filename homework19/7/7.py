from life import Home, Human, life
bhouse = Home()
hum1 = Human('Vitaliy', bhouse)
hum2 = Human('Boris', bhouse)
for i in range(365):
    if hum1.well_fed > 0:
        life(hum1, bhouse)
    if hum2.well_fed > 0:
        life(hum2, bhouse)
bhouse.print_info()
hum1.print_info()
hum2.print_info()
if (hum1.well_fed == 0) and (hum2.well_fed == 0):
    print('Оба умерли((((')
elif hum1.well_fed == 0:
    print('Жив только', num2.name)
elif hum2.well_fed == 0:
    print('Жив только', num1.name)
else:
    print('Оба живы, ура')

