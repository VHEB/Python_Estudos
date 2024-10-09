from functools import reduce

produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55.55},
    {'nome': 'p3', 'preco': 5.59},
    {'nome': 'p4', 'preco': 22},
    {'nome': 'p5', 'preco': 81.23},
]

soma = reduce(
    lambda acumulador, p: p['preco'] + acumulador,
    produtos,
    0
)
print(soma)

