salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = float(input('Quantos % de aumento para o funcionário? R$ '))
res = salario + (salario * aumento / 100)
print('O novo salario passará a ser R${:.2f}'.format(res))
