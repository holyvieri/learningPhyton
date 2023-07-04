somaIdade = 0
mediaIdade = 0
velhoH = 0
nomeVelho = 0
totMulher20 = 0
for p in range(1,5):
    print(f'------ {p}ª PESSOA -------')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaIdade += idade
    if p ==1 and sexo in 'Mm':
        velhoH = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > velhoH:
        velhoH = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 += 1

mediaIdade = somaIdade/p
print(f'A média de idade do grupo é de {mediaIdade} anos.')
print(f'O homem mais velho tem {velhoH} anos e se chama {nomeVelho}.')
print(f'Ao todo são {totMulher20} mulher(es) com menos de 20 anos.')