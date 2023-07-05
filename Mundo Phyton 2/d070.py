tot = totmil = menor = cont =  0
while True:
    produto = input('Nome do Produto: ')
    preço = float(input('Preço: R$ '))
    cont += 1
    tot += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi de R$ {tot:.2f}')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')