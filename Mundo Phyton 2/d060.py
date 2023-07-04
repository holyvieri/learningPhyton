#from math import factorial
num = int(input('Fatorial de: '))
#f = factorial(num)
n = num
f = 1
while n > 0:
    print(n, end='')
    print(' x ' if (n > 1) else (f' = {f}'), end='')
    f = f*n
    n = n-1
print(f'\n{num}! é {f}.')