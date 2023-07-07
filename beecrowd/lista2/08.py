n1, n2 = map(int, input().split())

if n1 == n2:
    print('O JOGO DUROU 24 HORA(S)')
elif n1 > n2:
    hour = 24 - (n1 - n2)
    print(f'O JOGO DUROU {hour} HORA(S)')
elif n2 > n1:
    hour = n2 - n1
    print(f'O JOGO DUROU {hour} HORA(S)')
'''In the case where n1 > n2, we want to calculate the duration when the game starts on one day and ends on the next 
 'day. To obtain this duration, we subtract n1 from 24 (representing 24 hours in a day) and then add n2.'''