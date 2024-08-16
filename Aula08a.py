#math = blibioteca
 #ceil = arredondamento para cima;
 #floor = arredondamento para baixo;
 #trunc = truncar o número, eliminar da vírgula pra frente;
 #pow = potência
 #sqrt = calcular raiz quadrada;
 #factorial = calcular o fatorial do número.
#'import math' importa todas as funções
#'from math import...' importa a função expecífica
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}.'.format(num,floor(raiz)))
