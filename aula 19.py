#criando um dicionario ou arquivo
pessoas = {'nome': 'joão', 'idade': 22, 'peso': 75}
#testes
print(pessoas)
print(pessoas['nome'],pessoas['idade'],pessoas['peso'])
print(f'{pessoas["nome"]} tém {pessoas["idade"]} anos e pesa {pessoas["peso"]}kg')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['altura'] = 1.75# pode se adicionar item deta forma, sem precisar do append
for k, v in pessoas.items():# laço de identifica chave ao valor contido na chave
    print(f'{k}: {v}')

paises = list()
pais = dict()
while True:
    pais['pais'] = str(input('adicione um pais ao aquivo: '))
    pais['estado'] = str(input('adicione o estado: '))
    pais['municipio'] = str(input('adicione o municipio: '))
    pais['bairro'] = str(input('adicione o bairrro: '))
    paises.append(pais.copy())
    pergunta = str(input('deseja adicionar uma nova região? sim ou não? '))
    if pergunta == 'sim':
        continue
    elif pergunta != 'sim':
        break
print(paises)
