distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem de {:.2f} km'.format(distância))
#if distância <= 200:
   # preço = distância * 0.50                      # maneira composta

#else:
    #preço = distância * 0.45
preço = distância * 0.50 if distância <= 200 else distância * 0.45 #maneira simplificada
print('O preço da sua passagem custara {:.2f} reais.'.format(preço))
