n = int(input())
x = [100, 50, 20, 10, 5, 2, 1]
print(n)
for d in x:
    notas = n//d # vai me dar a qntd inteira de notas qnd divido por algm numero da lista x
    n = n%d # vai atualizar o numero de n para quanto resta p ser dividido again
    frase = f'{notas} nota(s) de R$ {d:.2f}'.replace('.',',')
    print(frase)
