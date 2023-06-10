v = int(input('Qual é a velocidade atual do carro? '))
if (v > 80):
    print(f'Você foi MULTADO! A velocidade permitida é 80km/h, não {v}km/h\n'
          f'A multa custará R$ {float((v-80)*7):.2f}')
elif (v<80 and v>=40):
    print('Dirija com segurança e continue assim! Você está dentro do limite permitido!')
else:
    print('ACELERE com ponderação! A velocidade MÍNIMA permitida é 40km/h e a MÁXIMA é 80km/h!')

