# Analisador de Textos
nome = str(input('Digite seu nome completo: ')).strip()
print('Analizando seu nome...')
nc = nome.upper()
print('Seu nome em maiúsculas é: {}'.format(nc))
nn = nome.lower()
print('Seu nome em minúsculas é {}'.format(nn))
tl = len(nome)-nome.count(' ')
print('Seu nome tem ao todo {} letras'.format(tl))
pn = nome.find(' ')
print('Seu primeiro tem {} letras'.format(pn))