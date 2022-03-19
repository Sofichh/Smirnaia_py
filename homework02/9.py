number = int(input("Введите четырехзначное число: "))
thousands = number // 1000
hundreds = (number % 1000) // 100
dozens = (number % 100) // 10
units = number % 10
print(units, dozens, hundreds, thousands, sep='')
