preco = float(input('Preço dos produtos: R$ '))
print('FORMAS DE PAGAMENTO:\n[ 1 ] à vista dinheiro/cheque'
      '\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    print(f'A compra de R${preco:.2f} vai custar R${preco*0.9:.2f}')
elif opcao == 2:
    newPreco = preco * 0.95
    print(f'A compra de R${preco:.2f} vai custar R${newPreco:.2f}')
elif opcao == 3:
    parcelas= preco/2
    print(f'A compra será parcelada em 2x de R${parcelas} e continuará custando R${preco:.2f}')
else:
    tot = preco*1.20
    totparcela = int(input('Quantas parcelas? '))
    parcelas = tot / totparcela
    print(f'A compra será parcelada em {totparcela} vezes de {parcelas:.2f} e custará, no fim, R${tot:.2f} COM JUROS')


