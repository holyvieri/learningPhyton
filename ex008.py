m = float(input('Informe uma distância em metros: '))
print(f'A medida {m}m corresponde a:\n{m*(10**-3)}km\n{m*(10**-2)}hm\n{m*(10**-1)}dam\n{m*(10**1):.0f}dm\n{m*(10**2):.0f}cm\n{m*(10**3):.0f}mm')