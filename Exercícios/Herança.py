class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprimir(self):
        print('Classe Pessoa, ela é encontrada por último')
        print('Nome:', self.nome)
        print('Idade:', self.idade)

class Cliente(Pessoa):
    def imprimir(self):
        print('Classe Cliente, ela é encontrada primeiro')

class Aluno(Pessoa):
    pass

c1 = Cliente('Luiz', 32)
c1.imprimir()
a1 = Aluno('Maria', 22)
a1.imprimir()