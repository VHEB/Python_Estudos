from itertools import groupby
#Eles tem que estar ordenados para funcionar

alunos = [
    {'nome': 'Vitor', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'B'},
    {'nome': 'Miguel', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Eve', 'nota': 'B'},
    {'nome': 'Lara', 'nota': 'A'},
]

def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key= ordena)
grupos = groupby(alunos_agrupados, key=ordena)


for key, grupos in grupos:
    print(key)
    for aluno in grupos:
        print(aluno)
    