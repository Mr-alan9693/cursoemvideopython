altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
litros = area / 2
print('Para pintar uma parede de {:.2f}m2, você vai precisar de {:.1f} l de tinta'.format(area, litros))