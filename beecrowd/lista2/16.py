day_b = int(input().split()[1])
hour_b, min_b, sec_b = map(int, input().split(':'))
day_f = int(input().split()[1])
hour_f, min_f, sec_f = map(int, input().split(':'))

days = day_f - day_b
hours = hour_f - hour_b
mins = min_f - min_b
secs = sec_f - sec_b

if secs < 0:
    mins -= 1
    secs += 60
'''Nesse caso, subtraímos 1 minuto da variável mins e ajustamos o valor de secs adicionando 60. 
Ao adicionar 60 a secs, garantimos que a diferença seja calculada corretamente em termos de um minuto de 60 segundos.'''

if mins < 0:
    hours -= 1
    mins += 60
'''Ele verifica se mins é menor que 0, o que indica que o horário de término é anterior ao horário de 
início dentro da mesma hora. Nesse caso, subtraímos 1 hora da variável hours e ajustamos o valor de mins adicionando 60.
Ao adicionar 60 a mins, garantimos que a diferença seja calculada corretamente em termos de uma hora de 60 minutos.'''

if hours < 0:
    days -= 1
    hours += 24
''' Ele verifica se hours é menor que 0, o que indica que o horário de término é anterior ao horário 
de início dentro do mesmo dia. Nesse caso, significa que precisamos subtrair 1 dia da variável days e ajustar o valor 
de hours adequadamente. Ao adicionar 24 a hours, garantimos que a diferença seja calculada corretamente 
em termos de um período de 24 horas.'''

print(f'{days} dia(s)')
print(f'{hours} hora(s)')
print(f'{mins} minuto(s)')
print(f'{secs} segundo(s)')
