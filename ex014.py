import math
nu = float(input('digite um número fracionado:'))
print('a forma arredondada de {} é {:.2f}'.format(nu, math.ceil(nu)))
print(f'e parte inteira é {int(nu)}')
