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

#@property -> Permite criar métodos que podem ser acessados como atributos
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

#Um getter no modo pythonico
#Modo Pythonico é o modo mais correto de se fazer algo em Python -> Pythonic Way
# Setter -> Método que altera o valor de um atributo
# Getter -> Método que acessa o valor de um atributo


#_______________________________________________________________________________________________________________________



#Pilares da POO
"""
Encapsulamento -> Em POO, os detalhes de implementação de um objeto são escondidos e cada objeto interage com outros
objetos através de uma interface bem definida
Abstração -> Em POO, objetos do mundo real são representados computacionalmente
Herança -> Em POO, a ideia de herança é a capacidade de criar uma classe que herda atributos e métodos de uma classe
existente
Polimorfismo -> Em POO, polimorfismo é a capacidade de um objeto poder ser referenciado de várias formas
"""

#Encapsulamento
"""
Em Python, por convenção, é utilizado um underline para indicar que um atributo é privado
Python não tem modificadores de acesso
Por convensão é usando assim:
Sem underline -> Público
Um underline -> Protegido
Dois underlines -> Privado

_Protegido -> Só deve ser acessado por subclasses e classes
__Privado -> Só deve ser acessado pela própria classe
"""