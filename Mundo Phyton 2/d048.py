s = 0
cont = 0

for n in range(3, 501, 3):
    if n%2 != 0:
        cont = cont+1
        s += n
print(f' A soma de todos os {cont} valores solicitados é {s}')