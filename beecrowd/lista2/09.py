salary = float(input())

if salary <= 400.00:
    percent = 15
elif salary <= 800.00:
    percent = 12
elif salary <= 1200.00:
    percent = 10
elif salary <= 2000.00:
    percent = 7
else:
    percent = 4

new_salary = salary * (1 + percent / 100)
reajuste = salary * (percent / 100)

print(f'Novo salario: {new_salary:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {percent} %')
