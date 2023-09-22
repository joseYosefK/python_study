frase = str(input('descreva uma frase:')).upper().strip()
print('esta frase posui {} letras A'.format(frase.count('A')))
print('a primeira letra A aparece na posição de numero:{}'.format(frase.find('A')+1))
print('a ultima letra A aparece na posição de numero:{}'.format(frase.rfind('A')+1))
