# Dobro, Triplo, Raiz Quadrada
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
q = n ** (1/2) #raiz quadrada
#print('O dobro de {} vale {}'.format(n, d))
#print('O triplo de {} vale {}'.format(n, t))
#print('A raiz quadrada de {} vale {}'.format(n, q))
print('O dobro de {} vale {}'.format(n,(n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n,(1/2))))