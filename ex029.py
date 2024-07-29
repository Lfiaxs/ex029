v = float(input('Qual é a velocidade atual do carro? '))
if v>80:
    print('MULTADO! Você excedeu limite permitido que é de 80Km/h.')
    multa = (v-80)*7
    print('A multa vai custar R${:.2f}'.format(multa))
print ('Tenha um bom dia! Dirija com segurança')
