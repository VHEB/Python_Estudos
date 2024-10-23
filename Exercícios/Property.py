class Caneta:
    def __init__(self, cor, marca, preco):
        self.cor = cor
        self.marca = marca
        self.preco = preco

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError('Preço não pode ser negativo')
        self.__preco = valor

    def __str__(self):
        return f'Caneta {self.cor} {self.marca} que custa R${self.preco:.2f}'
    
c1 = Caneta('Azul', 'Bic', 5)
print(c1)