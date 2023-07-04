a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a1 + (10-1)* r
for i in range(a1, a10+r , r):
    print(f'{i}', end=' -> ')
print('FIM')