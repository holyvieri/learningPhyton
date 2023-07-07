values = input().split(' ')
a = float(values[0])
b = float(values[1])
c = float(values[2])
area_tri = (a*c)/2
pi = 3.14159
area_cir = (pi * (c**2))
area_trap = ((a+b)*c)/2
area_squa =  b**2
area_rec = a*b

print(f'TRIANGULO = {area_tri:.3f}\nCIRCULO = {area_cir:.3f}\n'
      f'TRAPEZIO = {area_trap:.3f}\nQUADRADO = {area_squa:.3f}\n'
      f'RETANGULO = {area_rec:.3f}')