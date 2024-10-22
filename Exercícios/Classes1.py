class Pessoa:
    def __init__(self, nome, idade, casado=False):
        self.nome = nome
        self.idade = idade
        self.casado = casado

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'
    
    def casar(self):
        if self.casado:
            print(f'{self.nome} já é casado(a)')
            return
        print(f'{self.nome} Casando...')
        self.casado = True
    
    def divorciar(self):
        if not self.casado:
            print(f'{self.nome} não é casado(a)')
            return
        print(f'{self.nome} Divorciando...')
        self.casado = False
    
p1 = Pessoa('Luiz', 29)
p1.divorciar()
p1.casar()
p1.casar()
p1.divorciar()