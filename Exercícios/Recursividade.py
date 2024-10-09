def recursiva(inicio=0, fim=10):
    
    print(inicio, fim)
    
    if inicio >= fim:
        return fim
    
    inicio += 1
    return recursiva(inicio,fim)
    
print(recursiva())

print(' ')

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
fac = factorial(5)
print(f'Resultado do factorial de 5 é {fac}')