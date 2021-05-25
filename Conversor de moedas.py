real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real/5.50
euro = real/8.99
iene = real/2.90
print ('Você pode comprar:\n {:.2f} dólar \n {:.2f} euro \n {:.2f} iene'.format(dolar, euro, iene))
