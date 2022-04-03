line = input('Введите текст: ')
dictionary = {}
for i in range(len(line)):
    dictionary[line.count(line[i])] = []
for i in range(len(line)):
    dictionary[line.count(line[i])].append(line[i])
lst = [i for i in dictionary.keys() if i != 1]
for i in lst:
    dictionary[i] = list(set(dictionary[i]))
for i in dictionary.keys():
    print(i, ':', dictionary[i], sep='')
