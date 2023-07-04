nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = float((nota1+nota2)/2)

print(f'Tirando {nota1} e {nota2}, a média do aluno é {media:.1f}')
if media <= 5.0:
    print('Você foi REPROVADO.')
elif 5.0 < media <= 6.9 :
    print(f'Você está em RECUPERAÇÃO.')
elif media >= 7.0:
    print(f'Você foi APROVADO.')