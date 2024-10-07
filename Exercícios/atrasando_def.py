def soma(a, b):
    return a + b
def multiplica(a, b):
    return a * b
def criar_func(funcao, x):
    def nova_func(y):
        return funcao(x, y)
    return nova_func

soma_2 = criar_func(soma, 2)
multiplica_2 = criar_func(multiplica, 2)
print(soma_2(3))  
print(multiplica_2(3))