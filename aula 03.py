# função para encontrar valor minimo na lista
'''def encotrar_minimo(lista):
    minimo = lista[0]
    for elem in lista:
        if elem < minimo:
            minimo = elem
    return minimo

lista_teste = [10, 5, 9, 7, 1, 2]
men = encotrar_minimo(lista_teste)
print('o menor é: [{}]'.format(men))'''
# função para somar lista
'''def somar_lista(lista):
    s = lista[0]
    for elem in lista:
       if elem != lista[0]:
         s += elem
    return s

lista_teste = [2, 6, 7, 8, 4]
total = soma(lista_teste)
print(total)'''

# função para definir numeros pares
'''def par(n):
    r = n % 2 == 0
    return r'''

# função para somar pares
'''def somar_pares(lista):
    s = 0
    for elem in lista:
       if par(elem):
         s += elem
    return s

lista_teste = [12, 5, 4 , 3, 8, 2]
soma = somar_pares(lista_teste)
print(soma)'''

#função para fatorar um numero
'''def fatorial(n):
  f = 1
  for i in range(1, n+1):
     f = f*i
  return f

num = 5
f = fatorial(num)
print(f)'''

# função para fatorial recursivco
'''def fatoria_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatoria_recursivo(n-1)

num = 5
f = fatoria_recursivo(num)
print(f)'''
# função para idenficar numeros primos
def num_primos(n):
     if n < 2:
         return False
     i = n//2
     while(i<1):
         if n % i == 0:
             return False
         i = i - 1
     return True
# funçãõ para mostrar mensagem na tela
def imprimir_resultado( numero, resultado):
    mensagem = f'o numero {numero} não é primo'
    if (resultado):
        mensagem = f'o numero {numero} é primo'
    return mensagem

numero = eval(input('digite um numero: '))
resultado = num_primos(numero)
mensagem = imprimir_resultado( numero, resultado)
print(mensagem)

