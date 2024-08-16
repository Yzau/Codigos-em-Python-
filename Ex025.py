#Procurando uma string dentro de outra
nome = str(input('Qual é seu nome? ')).strip()
print('Seu nome tem Araujo: {}'.format('araujo' in nome.lower()))