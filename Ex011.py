# pintando parede
larg = float(input('Largura da parade '))
alt = float(input('Altura da parede '))
área = larg * alt
print('Sua parede tem a dimensão de {}m x {}m e sua área de {}m².'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))