d = int(input('Quantos dias pretende alugar? '))
diaria = d*100.00
km = float(input('Quantos kms rodados? '))
kms = (km*1.50)+diaria
print('O total do aluguel do carro custará \033[0;31mR${:.2f}\033[m!'.format(kms))
