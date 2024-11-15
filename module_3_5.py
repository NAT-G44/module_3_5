def get_multiplied_digits(number):
    number = int(number)                 #преобразование убирает нули в начале числа
    str_number = str(number)             #преобразуем для того, чтобы обратиться к индексу
    first = int(str_number[0])


    while str_number.endswith('0'):        # до тех пор пока не оканчивается на 0
        str_number = str_number[:len(str_number)-1] #умножаем 1ую цифру на : начиная со 2ой
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
       return first
num = input('Введите целое число: ')
print(f'Произведение цифр числа {num} :', get_multiplied_digits(num))

    