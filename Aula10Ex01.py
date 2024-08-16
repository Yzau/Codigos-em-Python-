n1 = float(input('Digite sua prrimeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=7.0:
    print('Aprovado, Parabéns!!')
else:
    print('Reprovado, estude mais!!')