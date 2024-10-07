def decorador(funcao):
    def funcao_decorada():
        print('Antes da função')
        funcao()
        print('Depois da função')
    return funcao_decorada
@decorador
def minha_funcao():
    print('Minha função')
minha_funcao() 

#_______________________________________________________________________________________________________________________

def decoradora(func):
    print('Decoradora 1')

    def aninhada(*args, **kwargs):
        print('aninhada')
        res = func(*args, **kwargs)
        return res
    return aninhada
@decoradora
def soma(a, b):
    return a + b

print(soma(2, 3))
multiplica = decoradora(lambda a, b: a * b)
print(multiplica(10, 3))