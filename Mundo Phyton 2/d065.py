answer = 'S'
soma = quant = media = maior = menor = 0
while answer in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    answer = input('Quer continuar? [S/N] ').strip().upper()[0]
media = float(soma / quant)
print(f'Quantidade de números digitados: {quant}\nMAIOR VALOR: {maior}\nMENOR VALOR: {menor}\nMÉDIA: {media:.2f}')
