import json

CAMINHO_ARQUIVO = 'arquivo.json'

class Pessoa:
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('Vitor', 29)
p2 = Pessoa('Hugo', 32)
p3 = Pessoa('Maria', 35)
bd = [p1.__dict__, p2.__dict__, vars(p3)]

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False , indent=True)