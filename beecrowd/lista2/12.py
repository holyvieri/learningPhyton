salary = float(input())

taxes = {
    0: 'Isento',
    1: 0.08,
    2: 0.18,
    3: 0.28,
}

tax_amount = 0.0

if salary <= 2000.00:
    tax_amount = 0.0
elif salary <= 3000.00:
    tax_amount = (salary - 2000.00) * taxes[1]
elif salary <= 4500.00:
    tax_amount = (1000.00 * taxes[1]) + ((salary - 3000.00) * taxes[2])
else:
    tax_amount = (1000.00 * taxes[1]) + (1500.00 * taxes[2]) + ((salary - 4500.00) * taxes[3])

if tax_amount == 0.0:
    print('Isento')
else:
    print(f'R$ {tax_amount:.2f}')



