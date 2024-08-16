# Exercício 18 – Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(an,cosseno))
tangente = tan(radians(an))
print('O valor de {} tem a TANGENTE {:.2f}.'.format(an,tangente))