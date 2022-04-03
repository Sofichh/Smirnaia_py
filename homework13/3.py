size = int(input('Укажите размер файла для скачивания: '))
velocity = int(input('Какова скорость вашего соединения? '))
for i in range(size//velocity):
    print('Прошло ', i+1, ' сек. Скачано ', (i+1)*velocity, ' из ', size, ' Мб (', int(round((i+1)*velocity/size*100, 0)), '%)', sep='')
if size % velocity != 0:
    print('Прошло', size//velocity + 1, 'сек. Скачано', size, 'из', size, 'Мб (100%)')
