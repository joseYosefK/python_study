print(' digite dois numeros para uma comparação')
n1 = float(input('digite um numero: '))
n2 = float(input('digite outro numemro: '))
if n1 > n2:
    print(f'{n1} é maio e {n2} é menor')
elif n1 < n2:
    print(f'{n1} é o menor e {n2} é o maio ')
else:
    print(f'{n1} é igual a {n2}')