line = input('Введите строку из 10 символов, содержащую только a и b: ')
milk = 0
for i in range(10):
    if line[i] == 'b':
        milk += 2 * (i+1)
print('За день собрано столько литров молока: ', milk)
