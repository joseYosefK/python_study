nome = input('qual é o seu nome completo?')
print(nome.upper())
print(nome.lower())
nu_caracteris = (len(nome))
nu_espaços = nome.count(' ')
f_dividida =nome.split()
print('este nome possui {} caracteres'.format(nu_caracteris))
print('{} espaços'.format(nu_espaços))
print('E {} letras'.format(int(nu_caracteris)-int(nu_espaços)))
print('Primeiro nome:{} '.format(f_dividida[0]))
print('sobrenome: {}'.format(f_dividida[1]))