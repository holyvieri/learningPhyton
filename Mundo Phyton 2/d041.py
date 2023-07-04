from datetime import date
nasc = int(input('Informe o ano do seu nascimento: '))
atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'Com {idade} anos compete-se na faixa MIRIM')
elif idade <= 14:
    print(f'Com {idade} anos compete-se na faixa INFANTIL')
elif idade <= 19:
    print(f'Com {idade} anos compete-se na faixa de JUNIOR')
elif idade <= 25:
    print(f'Com {idade} anos compete-se na faixa SÊNIOR')
else:
    print(f'Com {idade} anos compete-se na faixa MASTER')