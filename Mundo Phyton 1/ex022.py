nome = str(input('Digite seu nome completo: ')).strip()
u = nome.upper()
l = nome.lower()
s = nome.split()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {u}\nSeu nome em minúsculas é {l}\n'
      f'Seu nome tem ao todo {(len(nome) - nome.count(" "))} letras\n'
      f'Seu primeiro nome é {s[0]} e ele tem {len(s[0])} letras')

