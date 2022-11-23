# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

y = 1
z = 0
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print("x y z")
            print(x,  y,  z)
            result = (not (x or y or z)) == (not x and not y and not z)
            if result == True:
                print("Утверждение истинно!")
            else:
                print("Утверждение ложно!")
