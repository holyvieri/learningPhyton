soma = 0
numPar = 0
for vezes in range(1, 7):
    n = int(input(f'Informe o {vezes} valor:'))
    if n%2 == 0:
        soma += n
        numPar += 1
print(f'Há {numPar} número(s) PAR(ES) e a soma deles é {soma}')
