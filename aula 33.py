'''def merge(vetor, ini, meio, fin):
    # separa 'vetor' nos 2 subvetores que serão mesclados
    esq_vetor = vetor[ini:meio + 1]  # subvetor esquerdo
    dir_vetor = vetor[meio + 1: fin + 1]  # subvetor direito
    # variáveis para controlar a iteração entre os subvetores
    i = 0  # índice do subvetor esquerdo
    j = 0  # índice do subvetor direito
    k = ini  # índice para a parte ordenada do vetor
    # percorrer ambos os subvetores até que um deles fique sem elementos
    while i < len(esq_vetor) and j < len(dir_vetor):
        # se o subvetor esquerdo tiver o menor elemento ele será colocado
        # na parte ordenada e o índice do subvetor esquerdo será incrementado
        if esq_vetor[i] <= dir_vetor[j]:
            vetor[k] = esq_vetor[i]
            i = i + 1
        # oposto ao anterior
        else:
            vetor[k] = dir_vetor[j]
            j = j + 1
        # incrementando o índice da parte ordenada
        k = k + 1
    # adicionar os elementos restantes no subvetor esquerdo, caso existam
    while i < len(esq_vetor):
        vetor[k] = esq_vetor[i]
        k = k + 1
        i = i + 1
    # adicionar os elementos restantes no subvetor direito, caso existam
    while j < len(dir_vetor):
        vetor[k] = dir_vetor[j]
        k = k + 1
        j = j + 1


def mergeSort(vetor, ini, fin):
    if ini >= fin:
        return

    meio = (ini + fin) // 2
    mergeSort(vetor, ini, meio)
    mergeSort(vetor, meio + 1, fin)
    merge(vetor, ini, meio, fin)


def main(vetor):
    mergeSort(vetor, 0, len(vetor) - 1)
    print("Vetor ordenado:", vetor)


# testando o algoritmo
vet = [27, 9, 5, 1, 20, -3]
main(vet)'''''

def megasorte(vector):
    meio = len(vector) // 2
    v_dic = vector[:meio+1]
    v_esc = vector[meio+1:]





vetor = [1, 3, 7, 2, 10, 20, 6]
direito = megasorte(vetor)
print(direito)