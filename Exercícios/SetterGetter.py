class Caneta:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print('chamando @property cor()')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('chamando setter cor()')
        self._cor = valor

c1 = Caneta('Azul')
c1.cor = 'Vermelho'
print(c1.cor)