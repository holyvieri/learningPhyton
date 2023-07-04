f = input('Digite uma frase: ').upper().strip()
print(f'A letra A aparece {f.count("A")}.\n'
      f'A primeira letra A apareceu na posição {f.find("A")+1}\n'
      f'A última letra A apareceu na posição {f.rfind("A")+1}')
