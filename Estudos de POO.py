#POO -> Programação Orientada a Objetos
"""
Classes -> Modelo do objeto do mundo real sendo representado computacionalmente
Atributos -> Características do objeto
Métodos -> Comportamento do objeto (funções)
Construtor -> Método especial para criar objetos
Objeto -> Instância da classe
Instância -> Objeto criado a partir de uma classe

Usamos PascalCase para nomear classes em Python
class NomeDaClasse:
    def __init__(self, atributos): -> Método construtor
        self.atributos = atributos -> Atributos do objeto

p1 = NomeDaClasse() -> Instância de um objeto

self -> Representa o próprio objeto

"""

#hardcoded -> Dados fixos no código (não é recomendado)

#Exemplo de classe
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

    def ligar_desligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

# __str__ -> Método especial que retorna uma string
    def __str__(self):
        return f'{self.voltagem}V está ligada: {self.ligada}'

#__dict__ -> Retorna um dicionário com os atributos do objeto
# print(l1.__dict__)
# vars(l1) -> Retorna um dicionário com os atributos do objeto

#Propriedades que começam com __ são privadas
#Propriedades que começam com @ são protegidas
"""
@classmethod -> Método de classe (não precisa de uma instância para ser chamado)
@staticmethod -> Método estático (não precisa de uma instância e nem da classe para ser chamado)

"""

#Metodos de Classe + Factory Method
class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero

    def sacar(self, valor):
        if valor > self.saldo + self.limite:
            print('Saldo insuficiente')
            return
        self.saldo -= valor
        self.detalhes()

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Número: {self.numero}\nSaldo: {self.saldo}\nLimite: {self.limite}')

    @staticmethod
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}