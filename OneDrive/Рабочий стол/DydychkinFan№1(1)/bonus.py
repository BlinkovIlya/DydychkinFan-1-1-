dead = int(input("Введите количество значений в массисве(считая от единицы): "))
inside = []
i = 1
while dead>0:
     i = str(i)
     ghoul = float(input("Введите число №"+i+": "))
     inside.append(ghoul)
     dead = dead-1
     i = int(i)
     i = i+1
print(inside)
lim = 10000000000000000000000000000000000000000000000000000000001
for z in range(len(inside)):
    s =  inside[z]
    if s<lim:
        lim=s
alpha = int(input("Введите число, которое отличается от минимального числа из массива: "))
l = 0
f =alpha+lim
for z in range(len(inside)):
    if inside[z]==f:
        l = l+1
print("Количество =", l)


    
