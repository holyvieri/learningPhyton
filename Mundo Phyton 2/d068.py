from random import randint
v=0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0,10)
    tot = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {player} e o computador {pc}. Total de {tot}.', end='')
    print('DEU PAR' if tot%2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if tot%2 == 0:
            print('Você GANHOU!')
            v+=1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if tot%2 == 1:
            print('Você VENCEU!')
            v +=1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes!')


