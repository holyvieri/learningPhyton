num = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha uma das bases para conversão:'
                  '\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL'
                  '\n[ 3 ] converter para HEXADECIMAL\nSua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')