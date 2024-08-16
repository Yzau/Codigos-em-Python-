# Radar eletrônico
velocidade = float(input('Qual a velocidade do carro ? '))
if velocidade > 80:
    print('MULATDO!!!, Você excedeu o limite permitido que é de 80Km/h.')
    multa = (velocidade - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
print('Dirija com segurança!')