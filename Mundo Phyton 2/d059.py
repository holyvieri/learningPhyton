num1 = int(input('Informe o primeiro valor: '))
num2 = int(input('Informe o segundo valor: '))
print('-==-'*10)
operacoes = 0
while not operacoes == 5:
    operacoes = int(input('\n[ 1 ] somar\n[ 2 ] multiplicar \n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n '
                          '>>>> Qual é a sua opção? '))
    if operacoes == 1:
        somar = num1 + num2
        print(f'O resultado de {num1} + {num2} = {somar}\n',end='-==-'*10)
    elif operacoes == 2:
        mult = num1 * num2
        print(f'O resultado de {num1} x {num2} = {mult}\n',end='-==-'*10)
    elif operacoes == 3:
        if num1 > num2:
            print(f'O maior valor informado é "{num1}"\n',end='-==-'*10)
        elif num2 > num1:
            print(f'O maior valor digitado é "{num2}"\n',end='-==-'*10)
        else:
            print('Os valores informados são iguais, portanto, não há um que seja maior que outro.\n',end='-==-'*10)
    elif operacoes == 4:
        num1 = int(input('Informe um novo valor: '))
        num2 = int(input('Informe um outro valor: '))
    else:
        print('Operação inválida, tente novamente.')