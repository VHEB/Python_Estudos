#Relação entre classes: Associação, Agregação e Composição
#Associação -> Uma classe usa a outra, mas sem que uma dependa da outra
#Agregação -> Uma classe usa a outra, mas precisa dela para funcionar uma determinda ação
#Composição -> Uma classe usa a outra, mas precisa dela para funcionar e a outra só existe dentro da primeira

#Agregração
class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def adicionar_produto(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.valor)
        print()

    def total(self):
        return sum([p.valor for p in self._produtos])

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

#Instâncias
carrinho = CarrinhoDeCompras()
p1, p2 = Produto('Camiseta', 50), Produto('Iphone', 10000)
carrinho.adicionar_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())