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