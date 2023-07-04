import random
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)

print('SUAS OPÇÕES:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))

if (jogador == 3) or (jogador > 3):
    print('JOGADA INVÁLIDA!!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!')
    print('-='*12)
    print(f'VOCÊ jogou {itens[jogador]}\nO COMPUTADOR jogou {itens[pc]}')
    print('-='*12)

    if pc == 0: # pedra
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCE!')
        elif jogador == 2:
            print('COMPUTADOR VENCE!')
    elif pc == 1: # papel
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCE!')
    elif pc == 2: # tesoura
        if jogador == 0:
            print('JOGADOR VENCE!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        elif jogador == 2:
            print('EMPATE!')


