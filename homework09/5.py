films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия',
         'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favourite = []
k = 0
numbers = int(input('Сколько фильмов хотите добавить? '))
for i in range(numbers):
    film = input('Введите название фильма: ')
    for i in films:
        if film == i:
            favourite.append(i)
            k += 1
    if k == 0:
        print('Ошибка: фильма', film, 'у нас нет :(')
    k = 0
print('Ваш список любимых фильмов:', ', '.join(favourite))

