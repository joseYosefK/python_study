# criando um arquivo
pessoa = []# lista temporaria
arquivo = []# arquivo a ser criado
while 'não':# laço
    pessoa.append(str(input('nome da pessoa: ')))#adicionando a lista
    pessoa.append(int(input('qual o peso da pessoa: ')))# adicionando a lista
    arquivo.append(pessoa[:])#criando uma copia da lista no arquivo, desvinculada da lista
    pessoa.clear()# apagando a lista
    # condicional de controle
    pergunta = input('deseja continuar? sim ou não? ')
    if pergunta == 'sim:':
        continue
    elif pergunta != 'sim':
        break
print(arquivo, '\n')
