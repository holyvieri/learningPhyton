num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}.')
elif num2 > num1:
    print(f'{num2} é maior que {num1}.')
else:
    print(f'Não existe valor maior, os dois informados são iguais.')
