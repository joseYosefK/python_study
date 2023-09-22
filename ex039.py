idade = int(input('Digite sua idade para saber se você já pode se alista: '))
if idade < 17:
    print('você deve se apresentar daqui à {} anos'.format(17 - idade))
elif idade == 17:
    print('você já pode se apresentar a uma junta militar')

elif idade == 18:
    print('você deve se apresentar a uma junta militar mais proxima.')
else:
    print('''você já esta passando {} anos da idades de se apresenta
     procure a junta militar mais proxima
     e regularize sua situação!'''.format(idade - 18))
