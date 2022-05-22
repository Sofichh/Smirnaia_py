from tax import Property, Apartment, Car, CountryHouse
summ = 0
money = int(input('Какой суммой вы располагаете? '))
ans = input('Есть ли у вас квартира? ').lower()
if ans == 'да':
    worthh = int(input('Введите стоимость вашей квартиры: '))
    home = Apartment(worthh)
    print('Налог на квартиру:', home.tax())
    summ += home.tax()
ans = input('Есть ли у вас машина? ').lower()
if ans == 'да':
    worthc = int(input('Введите стоимость вашей машины: '))
    car = Car(worthc)
    print('Налог на машину:', car.tax())
    summ += car.tax()
ans = input('Есть ли у вас дача? ').lower()
if ans == 'да':
    worthd = int(input('Введите стоимость вашей дачи: '))
    dacha = CountryHouse(worthd)
    print('Налог на дачу:', dacha.tax())
    summ += dacha.tax()
if money >= summ:
    print('Вы можете оплатить налоги')
else:
    print('Вам не хватает столько рублей: ', summ - money)