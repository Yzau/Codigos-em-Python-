# conversor de moedas
real = float(input('Quanto de dinheiro você tem na carteira ? R$'))
dolar = real / 4.95
euro = real / 5.38
print('R${:.2f} você pode comprar US${:.2f} e EUR${:.2f}'.format(real, dolar, euro))
