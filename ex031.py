distancia = float(input('qual a distancia em kilometros do perrcuso? '))
if distancia <= 200:
    print('esta viagem custara R$:{:.2f}'.format(distancia * 0.5))
else:
    print('esta viagem é mais longa, com o desconto custara R$:{}'.format(distancia * 0.45))
print('Tenha uma boa viagem')