from itertools import zip_longest

def zippper(lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zippper(l1, l2))

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='Sem cidade')))
