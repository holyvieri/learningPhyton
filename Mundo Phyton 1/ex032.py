import datetime
ano = int(input('Qual ano você quer analisar?\nOBS: Digite 0 para analisar o ano atual! '))
if ano == 0:
    ano = datetime.date.today().year #para pegar a data de hoje, o ano atual
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0) :
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO É BISSEXTO.')