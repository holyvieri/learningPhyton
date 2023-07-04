print(' GERADOR DE PA '.center(40, "-"))
a1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        cont +=1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
