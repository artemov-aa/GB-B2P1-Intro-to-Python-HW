# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coord_X = coord_Y = 0
while (coord_X == 0 or coord_Y == 0):
    coord_X = int(input('Введите ненулевую координату X: '))
    coord_Y = int(input('Введите ненулевую координату Y: '))
if (coord_X > 0 and coord_Y > 0):
    print('Точка с заданными координатами находится в I плоскости.')
elif (coord_X < 0 and coord_Y > 0):
    print('Точка с заданными координатами находится во II плоскости.')
elif (coord_X < 0 and coord_Y < 0):
    print('Точка с заданными координатами находится в III плоскости.')
elif (coord_X > 0 and coord_Y < 0):
    print('Точка с заданными координатами находится в IV плоскости.')
