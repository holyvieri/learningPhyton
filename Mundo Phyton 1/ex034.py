s = float(input('Qual é o valor do seu salário? '))
if s <= 1250:
    print(f'O salário era R$ {s} e agora passará a ser R$ {(s * 1.15):.2f}')
else:
    print(f'O salário era R$ {s} e agora passará a ser R$ {(s * 1.10):.2f}')