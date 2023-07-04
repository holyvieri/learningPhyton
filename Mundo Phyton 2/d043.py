p = float(input('Informe o seu peso em kg: '))
h = float(input('Informe sua altura em metros: '))
imc = p/(h**2)
print(f'Seu imc é {imc:.1f}\nCLASSIFICAÇÃO:')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc <= 40:
    print('OBSESIDADE')
else:
    print('! OBESIDADE MÓRBIDA !')