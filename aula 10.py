# multiplicção de matrizis;
def mult_MA(A, B):# definindo uma função para mutiplicação de matrizis
    nlinhasA = len(A)
    ncolunasA = len(A[0])
    ncolunasB = len(B[0])

    Ma_p= []

    for linha in range(nlinhasA):# percorrendo as linhas de A
        Ma_p.append([0])# começando uma linha em Ma_pa
        for coluna in range(ncolunasB):#percorrendo as colunas de B
            Ma_p[linha].append(0)
            for i in range(ncolunasA):# percorrendo as colunas de A
                Ma_p[linha][coluna] += A[linha][i]*B[i][coluna]# multiplicando as colunas de A x B
    return Ma_p# atribuindo o resultado a matriz Ma_p

M_A = [[1, 2 ,3], [1, 2, 3], [1, 2, 3]]
M_B = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
nova_m = mult_MA(M_A, M_B)
print(nova_m)
