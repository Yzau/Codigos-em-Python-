#Maior e menor valores
a = int(input('Primero valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
print('O menor valor foi {}.'.format(menor))
print('O maior valor foi {}.'.format(maior))
