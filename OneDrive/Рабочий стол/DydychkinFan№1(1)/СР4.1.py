from random import randint
dead = int(input("Введите количество значений в массисве(считая от единицы): "))
l = str(input("Генерируем случайно [Да/Нет]"))
inside = []
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
lim = -1000000000000000000000000
for z in range(len(inside)):
    s = inside[z]
    if s>lim:
        lim=s
for z in range(len(inside)):
            if inside[z]==lim:
                for j in range(z+1,p):
                    inside.pop(j)
                    inside.insert(j,0)
print(inside)

