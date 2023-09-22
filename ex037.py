print('digite um numero e escolha uma base de conversão; binaria, octal ou hexadecimal')
n = int(input('escolha um numero inteiro: '))
base = int(input(' digite 1 para binario, digite 2 para octal, ou 3 para hexadecimal: '))
if base == 1:
    print('{} em numeração binaria é igual a: {}'.format(n, bin(n)))
elif base == 2:
    print('{} convertido em base octal é igual a: {}'.format(n, oct(n)))
elif base ==3:
    print('{} convertido em base hexadecimal é igual a: {}'.format(n, hex(n)))
else:
    print('Digite uma opçâo valida')