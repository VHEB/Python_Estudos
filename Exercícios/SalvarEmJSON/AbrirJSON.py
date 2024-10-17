import json

with open('pessoa.json', 'r', encoding='UTF-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa))

    print(pessoa['tecnologias'])