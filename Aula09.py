#Fatiamento
#frase[9] = somente o caractere na posição 9
#frase[9:3] = somente os caracteres da posição 9 ao 12, o 13 não entra.
#frase[9:21:2] = somente os caracteres da posição 9 ao 21 mas pulando em 2 e 2
#frase[:5] = começa do caractere 0 e termina 5, mas não mostra o 5.
#frase[15:] = começa no 15 vai ate o final
#frase[9::3] = começa no 9 vai até o final e pulando de 3 em 3.

#análise
#len(frase) = mostra o comprimento da fase,ou  seja, as caracteres
#frase.count('o') = contar quantos as carecteres especificado
#frase.count('o',0,13) = contagem já com o fatiamento
#frase.find('deo') = encontra as caracteres na sequencia que foi digitada, caso o resultado retorne -1 a string não foi encontrada
#'curso' in frase = verificar se exite a palavra no frase, se sim retorna true

#tranformação
#frase.replace('Python','Android') = trocar a palavra pela outra.
#frase.upper() = colocar as letras em maiusculo
#frase.lower() = colacar as letras em menusculo
#frase.capitalize() = colacar todas as letras para menusculo menos a 1º letra da string
#frase.title() = colocar todas as 1º letras de cada palavra em maiusculo
#frase.strip() = remove todos os espaços inuteis no inicio e no fim
#frase.rstrip() = remove todos os espaços inuteis no final mantendo do inicio
#frase.lstrip() = remove todos os espaços inuteis no no inicio mantendo do final

#Divisão
#frase.split() = divide as palavras entre os espaços delas, gera um lista com as string

#Junção
#'-'.join(frase) = junta as string separadas colocando um separador'-'