w1 = input().lower()
w2 = input().lower()
w3 = input().lower()

if w1 == 'vertebrado':
    if w2 == 'ave':
        if w3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if w3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if w2 == 'inseto':
        if w3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if w3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
