try:
# recebendo um numero de testes
    t = int(input())
# testando se o numero eh maio que 0 e menor igual a 1000
    if 0 < t <= 1000:
#criando um laco de testes
        for i in range(t):
# tratando a entrada para numeros inteiros
            try:
# recebendo a quandidade de nimeros do array
                n = int(input())
# testando se o numero eh maior que 0 e menor igual a mil que 1000
                if 0 < n <= 1000:
# recebendo os numeros do array conjunto
                    conj = input()
#  convertendo para inteiros e retirando os espacos
                    conj = [int(i) for i in conj.split()]
# or denando os numeros no array
                    conj.sort()
# criando uma variavel para soma minima que nao pode ser jerada
                    resposta = 1
# criando um laco para cada caso de teste
                    for j in range(n):
# testando se a resposta ja eh o menor numero pois se for nao precisa mais ser testado
                        if conj[j] > resposta:
                            break
# se nao respos ta eh igual ou menor indicando que ja exeste e pode ser gerado
                        else:
                            resposta += conj[j]
# saida
                    print(resposta)
# tratamentos para entradas indevidas com str bools float e outros
                else:
                    break
            except:
                break
except:
    print('')