print(' BANKRUPT '.center(40,'-'))
valor = int(input('Qual o valor que você quer sacar? R$ '))
notas = [50, 20, 10, 1]
for nota in notas:
    qtdNotas = int(valor/nota) # vai me dar a qntd inteira de notas qnd divido por algm numero da lista x
    valor = valor - (qtdNotas * nota) # vai atualizar o numero do valor para quanto resta p ser dividido again
    print(f'{qtdNotas:.0f} nota(s) de R$ {nota:.2f}')
