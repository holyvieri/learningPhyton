from random import randint
pc_think = randint(0,5) #faz o pc pensar em um numero int entre 0 e 5
frase = ' Pensei em um número entre 0 e 5... Sabe qual é? Adivinha! '
print(f'{frase:¨^100}')
guess = int(input('Em qual número eu pensei? '))#jogador tenta adivinhar
if pc_think == guess:
    print(f"Parabéns! Pensei exatamente no número {pc_think}!")
else:
    print(f'Ah não! Não foi dessa vez... Você pensou {guess}, mas eu pensei {pc_think}!')
