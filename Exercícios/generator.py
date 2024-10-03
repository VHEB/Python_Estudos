import sys

lista = [n for n in range(100)]
generator = (n for n in range(100))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


def generator(n=0):
    yield n #Pausa aqui
    print('Pausa')
    yield n + 1
    print('Pausa 2') 
        

g = generator()
print(next(g))
print(next(g))

def generator2(n=0, max=10):
    while n < 100:
        yield n
        n += 1
        if n > max:
            return

g2 = generator2()
for n in g2:
    print(n)