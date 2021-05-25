casa= float(input('Qual o valor da casa: '))
salario= float(input('Qual o seu sálario: '))
anos= int(input('Quantos anos de financiamento: '))
prestacao= casa / (anos * 12)
minimo= salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end ="")
print(' a prestação será de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Financiamento APROVADO')
else:
    print('Financiamento NEGADO')
