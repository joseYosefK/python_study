#identicar e ajudar pessoas com diabetes,
# 1_imprimir( por gentileza primeiro utilizile um aparelho de aferir glicose)
# 2_pedir o valor da aferição da glicose
# 3_atribuir este valor a uma variavel
# 4_se o valor for menor que 120
#       imprimir( você esta diabetico)
# 5_ se não
#       imprima(sua glicose esta dentro dos padrões saldaveis, continui mantendo essa dieta!)
print('Por gentileza faça o aferimento de sua glicose.')
glicose = eval(input('Se já aferiu digite o resultado aqui: '))
if glicose >= 120:
    print('você esta diabético')
    print(' procure um medico e nutricionista para iniciar um tratamento, cuide-se!')
else:
    print('sua glicose esta dentro dos padrões saldaveis, continui mantendo essa dieta!')
    print('OBRIGADO!')

