# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

dot_A = []
dot_B = []
dot_A.append(int(input("Введите координату X точки A: ")))
dot_A.append(int(input("Введите координату Y точки A: ")))
dot_B.append(int(input("Введите координату X точки B: ")))
dot_B.append(int(input("Введите координату Y точки B: ")))
distance = ((dot_A[0] - dot_B[0])**2 + (dot_A[1] - dot_B[1])**2)**0.5
print(f'Расстояние между заданными точками равно: {round(distance, 3)}')
