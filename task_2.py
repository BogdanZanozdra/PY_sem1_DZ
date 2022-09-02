# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
x = int(input('Задайте значение x '))
y = int(input('Задайте значение y '))
z = int(input('Задайте значение z '))
result = (not (x or y or z)) == (not x and not y and not z)
if result == True:
    print("Утверждение истинно!")
else:
    print("Утверждение ложно!")
