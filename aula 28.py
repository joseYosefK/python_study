from datetime import date
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# um metodo de criar class
# criar um objeto pesssoa atraves do ano de nascimeto
    @classmethod
    def ano_nascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
# metodo estatico verificar se eh menor de idade
    @staticmethod
    def ehmaiorde_idade(idade):
        return idade >= 18

pe1 = pessoa('maria', 26)
pe2 = pessoa.ano_nascimento('ana', 2006)
print(pe1.idade)
print(pe2.idade)
print(pessoa.ehmaiorde_idade(17))
