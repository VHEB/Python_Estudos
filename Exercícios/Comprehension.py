produtos = [
    {"nome": "p1", "preco": 50},
    {"nome": "p2", "preco": 30},
    {"nome": "p3", "preco": 20},
    {"nome": "p4", "preco": 70},
    {"nome": "p5", "preco": 90},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    for produto in produtos
]

print(*novos_produtos, sep='\n')

#_____________________________________________________

produto = {
    'nome': 'caneta azul',
    'preco': 1.50,
    'categoria': 'papelaria',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

print(dc)

