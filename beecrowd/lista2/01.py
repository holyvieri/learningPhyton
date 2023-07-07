table = input().strip().split()
x_code = int(table[0])
y_qnt = int(table[1])
price = 0
if x_code == 1:
    price = 4
elif x_code == 2:
    price = 4.5
elif x_code == 3:
    price = 5
elif x_code == 4:
    price = 2
elif x_code == 5:
    price = 1.5
total = float(y_qnt*price)
print(f'Total: R$ {total:.2f}')