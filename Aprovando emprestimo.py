casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
anual = casa / anos
prestacao = (anual + (anual * 6 / 100)) / 12
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em  {} anos'.format(casa, anos), end =" ")
print(' a prestação será de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo pode ser concedido!')
else:
    print('Emprestimo NEGADO!')
