'''a, b, c = map(float, sorted(input().split()))
sides = [c, b, a]
a = sides[0]
b = sides[1]
c = sides[2]
print(a)
print(b)
print(c)'''
a, b, c = sorted(map(float, input().split()), reverse=True)
print(a)
print(b)
print(c)
if a + b > c and a + c > b and b + c > a:
    if a ** 2 == b ** 2 + c ** 2:
        print('TRIANGULO RETANGULO')
    elif a ** 2 > b ** 2 + c ** 2:
        print('TRIANGULO OBTUSANGULO')
    elif a ** 2 < b ** 2 + c ** 2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or c == a:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
