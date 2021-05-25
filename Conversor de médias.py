distancia = float(input('Digite a distância em metros: '))
km = distancia / 1000
hm = distancia / 100
Dam = distancia * 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print('A distância de {:.2F} metros equivale a:'.format(distancia))
print('{:.3f}km\n{:.2f}hm\n{:.2f}Dam\n{:.2f}dm\n{:.2f}cm\n{:.2f}mm.'.format(km, hm, Dam, dm, cm, mm))