from itertools import count
km = float(input('insira a quilometragem: '))
if km > 80:
    print('\033[0:31mvocê esta acima da velocidade permitida\033[m')
    multa = (km - 80) * 7
    print(f'\033[0:31me foi multado em R$;{multa}\033[m')
if km > 80:
    print('reduza a velocidade e dirija com segurança')
else:
    print('dirija com segurança e tenha um bom dia!')

