import random
names = []
for n in range(1, 5):
    name = input('Digite o nome do aluno: ')
    names.append(name) #use the append() method to add the names to the list
random.shuffle(names)
print(f'A ordem aleatória ficou: {names}')