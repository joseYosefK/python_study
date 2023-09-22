from random import choice
print('sorteio de alonos, descreva o nome dos alunos abaixo:')
al1 = input('nome do aluno 1:')
al2 = input('nome do aluno 2:')
al3 = input('nome do aluno 3:')
al4 = input('nome do aluno 4:')
lista = [al1, al2, al3, al4]
print(f' o aluno(a) soteado foi: {choice(lista)}')