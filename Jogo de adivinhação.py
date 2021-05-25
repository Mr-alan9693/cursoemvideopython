from random import randint
from time import sleep
computador = randint(0, 3) #faz o computador pensar
print('\033[32m-=-\033[m'*40)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('\033[32m-=-\033[m'*40)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('Processando...')
sleep(4)
if jogador == computador:
    print('\033[32mVocê coonsegui vencer, PARABÉNS!\033[m')
else:
    print('\033[31mVocê perdeu!\033[m')
print('--FIM==')



