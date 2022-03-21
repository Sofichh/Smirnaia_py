message = input('Введите сообщение: ')
step = int(input('Введите сдвиг: '))
lst = message.split()
new_message = []
new_word = []
alphabet = 'а,б,в,г,д,е,ё,ж,з,и,й,к,л,м,н,о,п,р,с,т,у,ф,х,ц,ч,ш,щ,ъ,ы,ь,э,ю,я'
alphabet1 = alphabet.split(',')
for k in range(len(lst)):
    for l in range(len(lst[k])):
        for i in (alphabet1):
            if lst[k][l] == i:
                if alphabet1.index(i) >= 33 - step:
                    new_word.append(alphabet1[alphabet1.index(i) + step - 33])
                else:
                    new_word.append(alphabet1[alphabet1.index(i) + step])
    line = ''.join(new_word)
    new_message.append(line)
    new_word = []
newmessage = ' '.join(new_message)
print('Зашиврованное сообщение:', newmessage)
