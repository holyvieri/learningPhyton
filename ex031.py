d = float(input('Qual é a distância da sua viagem? '))
preço = d * 0.50 if d <= 200 else d * 0.45
print(f'O preço da sua passagem será de R$ {preço:.2f}')

'''if (d <= 200):
    print(f'Para a distância de {d}Km, o preço da passagem é: R$ {(d * 0.50):.2f}')
else:
    print(f'Para a distância de {d}Km, o preço da passagem é: R$ {(d * 0.45):.2f}')'''