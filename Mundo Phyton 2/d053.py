frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
tudoJunto = ''.join(palavras)#substituir o espaço por nada
inversoFrase = tudoJunto[::-1]
'''inversoFrase= ''
for letra in range(len(tudoJunto)-1, -1, -1):
    inversoFrase += tudoJunto[letra]'''
print(f'{tudoJunto} -> {inversoFrase}')
if inversoFrase == tudoJunto:
    print('Palíndromo!')
else:
    print('Não é um Palíndromo')