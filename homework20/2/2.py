from karma import Karma, KillError, DrunkError, DepressionError, CarCrashError, GluttonyError
human = Karma()
while human.karma < 500:
    for i in range(1, 8):
        human.one_day(i)
print('Ваша карма составляет', human.karma)
print('Вы достигли просветления!')
