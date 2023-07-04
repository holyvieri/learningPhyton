from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade > 18:
    print(f'Você já deveria ter se alistado há {idade-18} anos.')
elif idade < 18:
    print(f'Ainda faltam {18-idade} para o alistamento.')
else:
    print('Já está na hora de se alistar!')
