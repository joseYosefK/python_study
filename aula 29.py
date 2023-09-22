# herança multipla
import datetime


class conta_poupaca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()
    def remumeracao_conta(self,saldo):
        self.saldo = saldo
        self.saldo += self.saldo + self.taxaremuneracao
