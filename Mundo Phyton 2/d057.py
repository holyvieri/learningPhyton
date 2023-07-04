sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]#tirei os espaços, joguei tudo p maiusculas e pego apenas a primeira letra
while sexo not in 'MmFf':
    sexo = input('Formato incompatível. Por favor, informe seu sexo [M/F]: ').strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso!')