valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qtdNotas = int(valor/nota) # vai me dar a qntd inteira de notas qnd divido por algm numero da lista x
    valor -= qtdNotas * nota # vai atualizar o numero de n para quanto resta p ser dividido again
    print(f'{qtdNotas:.0f} nota(s) de R$ {nota:.2f}')
print('MOEDAS:')
for moeda in moedas:
    valor = round(valor,2)
    qtdMoedas = int(valor/moeda)
    valor -= qtdMoedas * moeda  # atualiza o valor de n para quanto ainda resta
    print(f'{qtdMoedas:.0f} moeda(s) de R$ {moeda:.2f}')
