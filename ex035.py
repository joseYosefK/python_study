print('='*20)
print('identificador de possiveis triangolos')
print('='*20)
r1 = float(input('digite um valor: '))
r2 = float(input('digite outro valor: '))
r3 = float(input('digite outro valor: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('estes valores \033[0:36mFORMAM UM TRIANGOLO!\033[m')
else:
    print('estes valores \033[0:31mNÃO FORMAM UM TRIANGOLO.\033[m')
