# Напишите программу, которая по заданному номеру четверти, показывает 
# диапазон возможных координат точек в этой четверти (x и y).

quater = int(input('Введите номер четверти: '))
if quater < 1 or quater > 4:
    print('Нет такой четверти!')
if quater == 1:
    print('Диапазон возможных координат точек в этой четверти: Х > 0, Y > 0.')
if quater == 2:
    print('Диапазон возможных координат точек в этой четверти: Х < 0, Y > 0.')
if quater == 3:
    print('Диапазон возможных координат точек в этой четверти: Х < 0, Y < 0.')
if quater == 4:
    print('Диапазон возможных координат точек в этой четверти: Х > 0, Y < 0.')

