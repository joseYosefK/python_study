'''lista = []
for n in range(100):
    lista.append(n)
    total = 0
    for c in range(1, lista[n]+1):
        if lista[n] % c == 0:
            total += 1
    if total == 2:
        print(lista[n], 'eh primo')
    elif total >= 3:
        print(lista[n], 'nao eh primo')
    else:
        print(lista[n], 'nao eh primo')'''
entrada = []
for n in range(100):
    entrada.append(n)
    total = 0
    for c in range(1, entrada[n] + 1):
        if entrada[n] % c == 0:
            total = total + 1
    if total == 2:
        print(entrada[n], 'eh primo')
    elif total >= 3:
        print(entrada[n], 'nao eh primo')
    else:
        print(entrada[n], 'não eh primo')
