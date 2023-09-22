# vetores
'''vetor = [1, 2, 3, 4, 5]
for i in range(5):
    vetor[i] = vetor[i] + 2
print(vetor)'''
'''from typing import List, Any, Type

#criando vetores com entrada
numeros= list(range(10))
for n in numeros:
    numeros[n] = int(input('digite um numero: '))

for n in range(0, 10):
    if n % 2 != 0:
        print(numeros[n], 'par')
    elif n % 2 == 0:
        print(numeros[n], 'impa')'''

# calculo de media utilizando vetores
notas = [1, 2, 3, 4]
soma = 0
for i in range(4):
    notas[i] = float(input('dite a nota; '))
    soma = soma + notas[i]
    media = soma / 4
if media >= 5 and media < 7:
        print('este aluno vai pra recuperação')
elif media >= 7:
        print('este aluno foi aprovado')
else:
        print('este aluno esta reprovado')
print('A media do aluno é:{:1}'.format(media))

