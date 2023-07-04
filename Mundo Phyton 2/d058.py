from random import randint
pc = randint(0,10)
user = int(input('Qual será o valor que o computador pensou?! Tente adivinhar! É um número de 0 a 10. \nPALPITE: '))
cont = 0
acertou = False
while not acertou:
    user = int(input(f'Ah não! Ainda não é este número. Tente novamente: '))
    cont += 1
    if user == pc:
        acertou = True
    else:
        if user < pc:
            print('Mais...Tente mais uma vez!')
        elif user > pc:
            print('Menos...Tente mais uma vez!')
print(f'FIM DE JOGO!\n Você acertou em {cont} tentativas!')
