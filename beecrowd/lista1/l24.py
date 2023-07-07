def main(): #A função main() é definida para ser o ponto de entrada do programa.
    from sys import stdin, stdout #stdin e stdout do módulo sys para entrada e saída de dados.
    from collections import defaultdict #defaultdict do módulo collections para criar um dicionário com valores padrão.
    from operator import itemgetter #itemgetter do módulo operator para ordenar os itens do dicionário.
    from math import floor #floor da biblioteca math para arredondar um número para o menor inteiro.

    def truncate(f):#A função truncate(f) é definida para arredondar um número decimal para duas casas decimais.
        return floor(f * 100) / 100

    city = 1 #A variável city é inicializada com o valor 1. Ela será usada para representar o número da cidade.
    n = int(stdin.readline()) #Lemos um número inteiro n a partir da entrada padrão usando stdin.readline().
    # Esse valor indica a quantidade de leituras de consumo de água que serão feitas para a cidade atual.
    while True:
        consumptions = defaultdict(int) #Dentro do loop, criamos um dicionário vazio chamado consumptions usando
        # defaultdict(int). Esse dicionário será usado para armazenar o consumo de água por residência.
        total_consumption = total_residents = 0
        for _ in range(n): #Em seguida, entramos em um loop que itera n vezes (conforme lido anteriormente).
            # Essas iterações representam as leituras de consumo de água para cada residência.
            x, y = map(int, stdin.readline().split()) #Dentro do loop, lemos dois números inteiros x e y a partir da
            # entrada padrão usando stdin.readline(). Esses números representam a quantidade de residentes e
            # o consumo de água para a residência atual.
            consumptions[y // x] += x #Dividimos y por x para obter o consumo médio de água por residência e usamos
            # essa média como chave para o dicionário consumptions. Somamos x ao valor existente no dicionário usando o operador +=.
            total_consumption += y
            total_residents += x
        #Adicionamos x a total_residents e y a total_consumption para calcular o consumo total e o número total de residentes.

        #Fora do loop interno, escrevemos o número da cidade atual e um texto formatado usando stdout.write().
        #O texto inclui a chave e o valor de cada item do dicionário consumptions ordenado pelo valor (consumo médio)
        # usando sorted() e itemgetter(0).
        stdout.write(f'Cidade# {city}:\n')
        stdout.write(' '.join(f'{c[1]}-{c[0]}' for c in sorted(consumptions.items(), key=itemgetter(0))))
        stdout.write(f'\nConsumo medio: {truncate(total_consumption / total_residents):.2f} m3.\n')
        #Escrevemos o consumo médio formatado usando truncate(total_consumption / total_residents)
        # para arredondar o valor e limitar o número de casas decimais.

        n = int(stdin.readline()) #Lemos o próximo valor de n a partir da entrada padrão.
        if n == 0: #Se n for igual a zero, significa que não há mais cidades para processar, então saímos do loop usando break.
            break
        stdout.write('\n')#Escrevemos uma linha em branco usando stdout.write('\n')
        city += 1

main()




