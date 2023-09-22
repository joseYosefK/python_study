# driando e rstanciando claces
class Salario:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus

class Empregado:
    def __init__(self, nome, idade, Salario):
        self.nome = nome
        self.idade = idade
        self.Salario = Salario

    def salario_total(self):
        return self.Salario.salario_anual()


salario = Salario(int(input('valor do salario; ')), int(input('va~lor do bonus; ')))
emp = Empregado('jose', 37, salario)
print(emp.salario_total())
