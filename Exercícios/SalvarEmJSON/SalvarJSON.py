import json

pessoa = {
    "nome": "João",
    "sobrenome": "Silva",
    "idade": 25,
    "cidade": "São Paulo",
    'endereco': [
        {
            "rua": "Rua A",
            "numero": 100
        },
        {
            "rua": "Rua B",
            "numero": 200
        }
    ],
    'dev': True,
    'tecnologias': ['Python', 'JavaScript', 'C#']
}

with open('pessoa.json', 'w', encoding='UTF-8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)