print('\033[032m-=\033[m'*20)
print('Analisador de triângulos')
print('\033[031m-=\033[m'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('\033[32mOs três segmentos formam um triângulo!\033[m')
else:
    print('\033[31mOs três segmentos não formam um triângulo!\033[m')

