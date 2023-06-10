import random
frase = ' Analisador de Triângulos '
print(f'{frase:-^60}')
n = []
for i in range(3):
    i = float(input('Segmento: '))
    n.append(i)
if (n[0] < n[1] + n[2]) and (n[1] < n[2] + n[0]) and (n[2] < n[1] + n[0]):
    print(f'Os segmentos {n} PODEM FORMAR triângulo!')
else:
    print(f'Os segmentos {n} NÃO PODEM FORMAR triângulo!')