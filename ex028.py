from random import randint
n = randint(0, 5)
print('vou pensar em um numero de 0 a 5')
chute = int(input('adivinha que numero eu pencei?'))
if chute== n:
    print('\033[0:33mparabéns você acertou\033[m!')
else:
    print('\033[0:31meu ganhei, você errou!\033[m')


