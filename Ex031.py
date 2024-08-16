#Custo da Viagem
viagem = float(input('Qual é a distancia da sua viagem ? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(viagem))
if viagem <= 200:
    valor = (viagem * 0.50)
    print('E o preço da sua passagem será de R${:.2f}'.format(valor))
else:
    valor = (viagem * 0.45)
    print('E o preço da sua passagem será de R${:.2f}.'.format(valor))