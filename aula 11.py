# trabalhando com listass
try:
    lista = ['português', 'matematica','ciência','geografia']
    item = input('qual materia você procura?\n')
    item = lista.index(item)# identificando posição na lista
    print(f'a materia esta na posição :{item} da lista')
except:# tratando excessões
    print('materia não encontrada na lista')
    per = input('deseja inseerir a materia? sim ou não:\n')
    if per == 'sim':# adicionado novo a lista
        novo = input('digite a nova materia:\n')
        lista.append(novo)
        print(lista)