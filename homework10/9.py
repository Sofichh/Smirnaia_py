nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
lst = [nice_list[k][i][j] for k in range(2) for i in range(3) for j in range(3)]
print('Ответ:', lst)
