#ogo da Adivinhação v.1.0
from random import randint
from time import sleep
computador = randint(0 ,5) #faz o computador sortiar o numero
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))
print('PROCESSANDO...')
sleep(5)
if jogador == computador:
    print('Você ganhou!!! ')
else:
    print('Perdeu!!! HAHAHAHA, pensei no número {} e não no {}.'.format(computador,jogador))