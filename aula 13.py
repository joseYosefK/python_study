# trabalhando com filas
fila = [i for i in range(1, 11)]#adicionando numeros a fila
print(fila)
#[1, 2, 3, 4, 5, 7, 8, 9, 10]
fila.append(4)#     ← último elemento inserido
print(fila)
#[1, 2, 3, 5, 6, 7, 8, 9, 10, 4]
fila.pop(0)
#1     ← retorna e remove o primeiro elemento
print(fila)
#[2, 3, 4, 6, 7, 8, 9, 10, 4]     ← o 2 passa a ser o primeiro elemento
fila.pop(0)
#2     ← retorna e remove o primeiro elemento
print(fila)
#[3, 4, 4, 5, 6, 7, 8, 9, 10, 4]     ← o 3 passa a ser o primeiro elemento