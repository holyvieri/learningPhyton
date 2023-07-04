import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
#h = math.sqrt((co**2) + (ca**2))
h = math.hypot(co, ca)
print(f'A hipotenusa vai medir {h:.2f}')
