alphabet = 'abcdefg'
print('Копия:', alphabet[:])
print('В обратном порядке:', alphabet[::-1])
print('Каждый второй элемент(включая самы первый):', alphabet[0:7:2])
print('Каждый второй элемент псоле первого:', alphabet[1:7:2])
print('Все элементы до второго:', alphabet[:1])
print('Все элементы, начиная с конца до предпоследнего:', alphabet[:-2:-1])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 4):', alphabet[3:4])
print('Последние три элемента строки:', alphabet[-3:])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 5):', alphabet[3:5])
print('Все элементы в диапазоне индексов от 3 до 4 (не включая 5) в обратном порядке:', alphabet[-3:-5:-1])