code = input('Введите зашифрованное сообщение: ')
deciphered_word = []
for i in range(0, len(code), 2):
    deciphered_word.append(code[i])
if len(code) % 2 != 0:
    for i in range(-2, -len(code), -2):
        deciphered_word.append(code[i])
else:
    for i in range(-1, -len(code), -2):
        deciphered_word.append(code[i])
print('Расшиврованное сообщение:', ''.join(deciphered_word))
