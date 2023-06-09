info = input('Informe algo a ser analisado: ')
print(f'O tipo primitivo desse valor é {type(info)}')
print(f'É espaço? {info.isspace()}')
print(f'É um número? {info.isnumeric()}')
print(f'É alfabético? {info.isalpha()}')
print(f'É alfanumérico? {info.isalnum()}')
print(f'Está em minúsculas? {info.islower()}')
print(f'Está em maiúsculas? {info.isupper()}')
print(f'Está capitalizada? {info.istitle()}')


