import saude
print(' digite as seguintes informações para saber com esta sua saúde.')
pressão = saude.pres_art(diasta=int(input('quanto deu sua pressão minima? ')),
                   sistoli=int(input('e a maxima? ')))
print(pressão)
pessoa = saude.imc(peso=float(input('quanto você pesa: ')), altura=float(input('qual é sua altura: ')))
if pessoa < 18.5:
    print(f'imc = {pessoa} está abaixo do peso')
elif pessoa < 25:
    print(f'imc={pessoa} você esta no peso ideal')
elif pessoa < 30:
    print(f' imc= {pessoa} você esta acima do peso')
else:
    print(f'imc= {pessoa} estado de obesidade')
