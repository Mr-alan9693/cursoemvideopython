velocidade = float(input('Qual é a velocidade atua do carro? '))
if velocidade > 80:
    print('\033[0;31mMULTADO\033[m, você passou o limite permitido que é de \033[31m80km/h\033[m!')
    multa = (velocidade-80) * 6
    print('Você deve pagar R$ {:.2f} reais de multa.'.format(multa))
else:
    print('\033[32mTenha um bom dia, dirija com segurança!')
