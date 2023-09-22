salario = float(input('qual o valor do salario atual?'))
almento = float(input('quanto por cento ouve de almento?'))
novo_s = salario+((salario/100)*almento)
print('Você passará a receber {} reais'.format(novo_s))
