def print_iter(interator):
    print(*list(interator), sep='\n')

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
]

novos_produtos = filter(lambda p: p['preco'] > 20, produtos)
print_iter(novos_produtos)