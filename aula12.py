'''lista = []# criando uma lista vasia
for i in range(10):# definindo o espaço da lista
    lista.append(int(input('digite um numero:')))# adicionando n a lista
    nova_lista = [i for i in lista if i % 2 == 0]# criando uma nova lista com base na primeira
print('esses são os numeros pares:',nova_lista)'''

# trabalhando com medias
'''lista = []
for i in range(4):
    lista.append(float(input('digite uma nota:')))
    media = sum(lista)/len(lista)
if media >= 7:
    print('Aluno aprovado sua media foi:', media)
elif media >= 5 and media < 7 :
    print('Este aluno deve faser uma recuperação sua media foi', media)
else:
    print('aluno reprovado, media:', media)'''

# trabalhando com pilhas
pilha = []#criando uma pilha vasia
#
for i in range(int(input('quantos elemetos tem esta pilha: '))):
    pilha.append(int(input('digite um numero')))
print(pilha)
perguta = input('deseja diminuir a pilha? sim ou não: ')
if perguta == 'sim':
    pilha.pop()
    print(pilha)
elif perguta == 'não':
    print(pilha)
    print('pilha salva com sucesso!')


