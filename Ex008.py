# conversor de medidas
medida = float(input('Uma distância em metros '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {:.1f}m corresponde a {}km, {}hm, {}dam,'.format(medida, km, hm, dam))
print('{}dm, {}cm e {}mm'.format(dm, cm, mm))
