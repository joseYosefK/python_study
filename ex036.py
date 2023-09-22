salari = float(input('qual o valor da sua renda memsal? '))
casa = float(input('Qual o valor do imovel? '))
anos = float(input('em quantos anos você pretende financiar o imovel? '))
prestaçâo = (casa / anos) / 12
if prestaçâo <= (salari / 100) * 30:
    print('\033[1:32mparabens você pode financiar este imovel\033[m')
    print(f'Com uma parcela de R$:{prestaçâo:.2f}')
else:
    print('\033[1:31minfelismente nestas condiçõs seu financiamento nâo pode ser aprovado.\033[m')
    print('Sujiro almentar o praso de pagamento')