nun =int(input('Digite um numero de 5 digitos:'))
u = nun // 1 % 10
d = nun // 10 % 10
c = nun // 100 % 10
m = nun // 1000 % 10
d_ml = nun // 10000 % 10
print('Analizando este numero temos:')
print('unidade:{}'.format(u))
print('Desena:{}'.format(d))
print('Centena:{}'.format(c))
print('unidade de milhar:{}'.format(m))
print('desena de milha:{}'.format(d_ml))