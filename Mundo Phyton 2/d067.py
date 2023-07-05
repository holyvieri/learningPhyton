while True:
    n = int(input('Quer ver a tabuada de qual valor [Número negativo para parar] ? '))
    negativo = str(n)
    if negativo[0] == '-':
        break
    print('-'*30)
    for i in range(1,11):
        mult = n * i
        print(f'{n} x {i} = {mult}')
        i += 1
    print('-'*30)
print('Programa ENCERRADO. Volte sempre!')
