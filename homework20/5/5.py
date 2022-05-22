from car import Bus
avtik = Bus(1, 5, 45, 0)
npas = avtik.move(1000, 5)
avtik.enter(npas)
avtik.exit(2)
avtik.move(3200, avtik.enter(2))
print('Заработано денег:', avtik.money)
