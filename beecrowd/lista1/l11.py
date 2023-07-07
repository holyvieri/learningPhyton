#product1
s1 = input().split(' ')
p1 = int(s1[0])
units_p1 = int(s1[1])
price_u_p1 = float(s1[2])
#product2
s2 = input().split(' ')
p2 = int(s2[0])
units_p2 = int(s2[1])
price_u_p2 = float(s2[2])
#total
t = (units_p1*price_u_p1) + (units_p2*price_u_p2)
print(f'VALOR A PAGAR: R$ {t:.2f}')