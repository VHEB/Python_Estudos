from itertools import combinations, product, permutations

def print_iter(interator):
    print(*list(interator), sep='\n')

l1 = [
    ['Vitor', 'Lucas', 'Miguel'],
    ['Maria', 'Ana', 'Eve', 'Lara'],
    
    ]
l2 = ['Maria', 'Ana', 'Eve', 'Lara']

print_iter(combinations(l1, 2))
print('Acabou o combinations')
print_iter(permutations(l2, 2))
print('Acabou o permutations')
print_iter(product(*l1))
print('Acabou o product')


camisetas = [
    ['vermelha', 'verde', 'azul'],
    ['P', 'M', 'G', 'GG'],
    ['algodão', 'poliéster'],
    ['masculina', 'feminina'],
]

print_iter(product(*camisetas)) #todas as combinações de camisetas possíveis