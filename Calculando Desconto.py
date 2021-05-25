preço = float(input('Qual é o preço do produto: R$ '))
desconto = int(input('Qual o valor do desconto R$ '))
novo = preço - (preço * desconto / 100)
print ('O preço do produto que custava R${:.2f},com {}% custará R${:.2f}'.format(preço,desconto, novo))
