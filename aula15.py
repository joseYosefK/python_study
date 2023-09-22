#trabalhando som conjuntos
print('percorrendo um conjunto')
conjunto = {'a', 1, 2020, (28, 12), 'a'}    # ← itens duplicados são automaticamente removidos
for elemento in conjunto:
    print(elemento)
'''1
(28, 12)
2020
a'''
print('adicionando novos objetos ao conjunto')
#adicionando novos objetos ao conjunto
conjunto = set()
conjunto.add(1)
conjunto.add(2)
print(conjunto)
#{1, 2}
conjunto.add(2)#     ← por não conter itens duplicados, a inserção é ignorada
print(conjunto)
#{1, 2}
print('removendo objetos do conjunto')
# remover objetos do conjuto
conjunto = {1, 2, 3}
conjunto.discard(1)
conjunto.remove(2)
print(conjunto)
{3}
conjunto.discard(5)#     ← o elemento 5 não existe!
#conjunto.remove(5)
'''Traceback (most recent call last):
File "<stdin>", line 1, in <module>
KeyError: 5'''
conjunto.clear()
print(conjunto)
#{ }
print('removendo objetos do conjunto de forma aleatoria')
#estraindo objetos do conjunto de forma aleatoria
conjunto = {'a', 1, 2, 3}# conjuto
conjunto.pop()# metodo de retirada aleatoria
print(conjunto)
#{1, 'a', 2, 3} este exemplo pode variar pois a retirada é aleatoria
conjunto.pop()
print(conjunto)
#{'a', 2}este exemplo pode variar pois a retirada é aleatoria
print('operando conjuntos')
# operando conjuntos
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}
uniao = conjunto_a.union(conjunto_b)
print(uniao)
#{1, 2, 3, 4, 5}
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)
#{3}
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)
#{1, 2}