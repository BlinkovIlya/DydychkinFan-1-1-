from random import randint
dead = int(input("Введите количество значений в массисве(считая от единицы): "))
l = str(input("Генерируем случайно [Да/Нет]"))
inside = []
r = []
p = dead
i = 1
if l == 'Нет':
    while dead>0:
         i = str(i)
         ghoul = float(input("Введите число №"+i+": "))
         inside.append(ghoul)
         dead = dead-1
         i = int(i)
         i = i+1
if l == 'Да':
    while dead>0:
        inside.append(randint(-1000000000000000000000000000, 1000000000000000000000000000000))
        dead = dead-1
print(inside)
dead3 = int(input("Введите количество значений в массисве(считая от единицы): "))
l3 = str(input("Генерируем случайно [Да/Нет]"))
inside3 = []
p3 = dead3
i3 = 1
if l3 == 'Нет':
    while dead3>0:
         i3 = str(i3)
         ghoul3 = float(input("Введите число №"+i3+": "))
         inside3.append(ghoul3)
         dead3 = dead3-1
         i3 = int(i3)
         i3 = i3+1
if l3 == 'Да':
    while dead3>0:
        inside3.append(randint(-1000000000000000000000000000, 1000000000000000000000000000000))
        dead3 = dead3-1
print(inside3)
for z in range(len(inside)):
    for z3 in range(len(inside3)):
        if inside[z]==inside3[z3]:
            r.append(inside[z])
print(list(set(r)))


