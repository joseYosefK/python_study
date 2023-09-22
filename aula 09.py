# defindo um vetor, e criando iteração com vetores
from numpy import array # importando a biblioteca
notas_real = array([2, 5, 10, 20, 50, 100], dtype=int) # definindo o vetor
print(notas_real)# testando o primeiro comando
troca = int(input('Digite um numero inteiro: '))# criando uma variavel para iteraçao
for i in range(6):# iniciando o laço
    if notas_real[i] < troca:# criando a condição de iteração
        notas_real[i] = troca # efetuando a iteração
print(notas_real)# testando o resultado
# obs; um vetor tambem funciona com strg desde que seja declarado o tipo de foma omogenea