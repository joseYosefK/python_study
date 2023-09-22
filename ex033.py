n1 = int(input('digite um número: '))
n2 = int(input('digite outro número: '))
n3 = int(input('digite outro número: '))
# vericão do maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maio valor é: {}'.format(maior))
# verificando o menor valor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(' o menor valor é:{}'.format(menor))




