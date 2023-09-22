salario = float(input('qual o valor do salario? '))
if salario >= 1250:
    almento = salario + (salario / 100)*10
else:
    almento = salario + (salario / 100)*15
print('você para a receber R$: {}'.format(almento))

