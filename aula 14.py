#trabalhando com tuple

'''nomes = {('joão', 'maria'): 1, ('josé', 'francisco'): 2, ('paulo', 'lucas'): 3}
print(nomes[('joão','maria')])'''

#dando atribuições a valores em tuple
from collections import namedtuple# criando uma coleção de uma tupla
pessoa = namedtuple('pessoa', 'nome peso idade altura')# definindo as coleções
joão = pessoa(nome='joão', peso=85, idade=40, altura=1.67)# atribuindo valores as coleções
print(joão.altura)