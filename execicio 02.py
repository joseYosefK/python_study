class veiculo:
    def __init__(self, nome, velocidade, qp_por_litros):
        self.nome = nome
        self.velocidade = velocidade
        self.qp_por_litros = qp_por_litros
    def resultado(self):
        print(f'veiculo; {self.nome}\n velocidade maxima; {self.velocidade}\n '
              f'quilometros por litros:{self.qp_por_litros}')


class onibus(veiculo):
    pass

modelo = onibus(input('nome do carro; '), int(input('velocidade maxima; ')),
                       int(input('quilometros por litro; ')))
modelo.resultado()

modelo_carro = veiculo(input('nome do carro; '), int(input('velocidade maxima; ')),
                       int(input('quilometros por litro; ')))
modelo_carro.resultado()
