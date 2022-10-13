# Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('X Y Z |\t¬(X ⋁ Y ⋁ Z)\t| (¬X ⋀ ¬Y ⋀ ¬Z) | ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
print('-' * 70)
for x in range(2):
        for y in range(2):
            for z in range(2):
                left_part = not (x or y or z) 
                right_part = not x and not y and not z
                print(f'{x} {y} {z} |\t{left_part}\t\t| {right_part}\t\t | {left_part == right_part}')