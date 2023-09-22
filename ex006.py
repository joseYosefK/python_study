A = input('Qual o nome do aluno?')
n1 = float(input('Digite a nota do 1° bimestre:'))
n2 = float(input('Digite a nota do 2° bimestre:'))
n3 = float(input('Digite a nota do 3º bimestre:'))
n4 = float(input('Digite a nota do 4º bimestre:'))
m =(n1+n2+n3+n4)/4
print('A media anual do aluno(a) {} é: {:.1f} '.format(A, m))
if m >=7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
