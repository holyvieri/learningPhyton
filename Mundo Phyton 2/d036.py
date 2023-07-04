valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
qnt_ano = int(input('Anos de financiamento: '))

prestacao_mensal = valor_casa/(qnt_ano*12)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {qnt_ano} anos, a prestação será de {prestacao_mensal:.2f} por mês.')
if prestacao_mensal > (1.30*salario):
    print(f'Seu empréstimo foi NEGADO.')
else:
    print(f'Seu empréstimo foi APROVADO!')
