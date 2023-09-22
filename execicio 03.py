# trabalhando com funçoes puras
# exemplo de funcao nao pura
'''va = 20

def mutiplica(fator):
    global va
    va = va * fator
    print('valor', va)

def main():
    n = int(input())
    mutiplica(n)
    mutiplica(n)

if __name__ == '__main__':
    main()

# em tempo real
# xexemplo de funcao pura
v = 20

def multiplicareal(v, f):
    v = v * f
    return v

def main():
    n = int(input())
    print('valor', multiplicareal(v, n))
    print('valor', multiplicareal(v, n))

if __name__ == '__main__':
    main()'''''

''' exercicio 03 , diferenças entre funcoes puras de funcoes nao puras
# coletando dados com input
v = input()
# retirando os espaços em branco e transformando em inteiros
v = [int(i) for i in v.split()]

def altera_lista(lista):
    lista[2] = lista[2] + 10
    return lista

def main():
    print('valores da lista', altera_lista(v))
    print('valores da lista', altera_lista(v))

if __name__ == '__main__':
    main()'''

# exemplo de funçoes puras
# recebendo os valores com input
'''v = input()
# retitando os espacos e transformando em inteiros
v = [int(i) for i in v.split()]
# criando a funcao para alterar valores sem interferir na lista original
def altera_valores(lista):
    no_lista = v[:]
    no_lista[2] = no_lista[2] + 10
    return lista

def main():
    print('nova lista', altera_valores(v))
    print('nova lista', altera_valores(v))
if __name__ == '__main__':
    main()'''


# script funcao5.py
def multiplicar_por(multiplicador):
    def multi(multiplicando):
        return multiplicando * multiplicador

    return multi

v = input()
v = [int(i) for i in v.split()]
m1 = v[0]
m2 = v[1]
def main():
    multiplicar_por_10 = multiplicar_por(m1)
    print(multiplicar_por_10(1))
    print(multiplicar_por_10(2))

    multiplicar_por_5 = multiplicar_por(m2)
    print(multiplicar_por_5(1))
    print(multiplicar_por_5(2))


if __name__ == "__main__":
    main()