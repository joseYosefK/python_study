nome = str(input('qual é o seu nome?')).strip()
sep = nome.split()
print('seu primeiro nome é:{}'.format(sep[0]))
print('seu iltimo nome é: {}'.format(sep[len(sep)-1]))
