#Funções
"""
Uma função é um bloco de código que realiza uma tarefa específica. 
Funções ajudam a organizar e reutilizar código, tornando-o mais modular e legível.
Parâmetros são variáveis listadas na definição de uma função. 
Eles permitem que você passe informações para a função.
Argumentos são os valores reais que você passa para a função quando a chama. 
Eles são atribuídos aos parâmetros correspondentes na definição da função.

Exemplo:
def minha_funcao(parametro1, parametro2):
    # Código da função
minha_funcao(argumento1, argumento2)

Argumentos posicionais -> A ordem dos argumentos importa -> minha_funcao(0, 0)
Argumentos nomeados -> A ordem dos argumentos não importa -> minha_funcao(parametro2=0, parametro1=0)
Argumentos padrão -> Valores padrão para argumentos -> def minha_funcao(parametro1=0)

_____________________________________________________
"""
#Retorno de valores
"""
Retornar valores de uma função com a palavra-chave return.
Se a função não tiver um return, ela retornará None.
Você pode retornar qualquer tipo de dado de uma função.
return interrompe a execução da função.
def minha_funcao():
    return "Olá Mundo"
_____________________________________________________
"""
#Escopo
"""
Escopo é o contexto em que variáveis e objetos existem.
Variáveis definidas dentro de uma função não são acessíveis fora dela.
Variáveis definidas fora de uma função são acessíveis dentro dela.

Variável global -> Variável definida fora de uma função
Variável local -> Variável definida dentro de uma função

global -> Palavra-chave que permite modificar uma variável global dentro de uma função.
def minha_funcao():
    global variavel_global
    variavel_global = 10
_____________________________________________________
"""
#Funções aninhadas
"""
Funções podem ser definidas dentro de outras funções.
Funções aninhadas podem acessar variáveis da função pai.
Funções aninhadas são usadas para evitar a repetição de código.
def funcao_pai():
    def funcao_filha():
        return "Olá Mundo"
    return funcao_filha()
_____________________________________________________
"""
#Empacotamento
"""
*args -> Parâmetro que permite passar um número variável de argumentos para uma função.
**kwargs -> Parâmetro que permite passar um número variável de argumentos nomeados para uma função.
def minha_funcao(*args, **kwargs):
    print(args)
    print(kwargs)
"""

#high order functions
#Funções que aceitam outras funções como argumentos ou retornam funções.

#Closure
"""
Uma closure é uma função que retorna outra função.
A função interna tem acesso às variáveis locais da função externa.
Closures são usadas para encapsular comportamentos relacionados.
def funcao_pai():
    variavel = 10
    def funcao_filha():
        return variavel
    return funcao_filha
_____________________________________________________
"""
#Dicionários
"""
Dicionários são coleções de dados que armazenam pares chave-valor.
Dicionários são mutáveis.
Dicionários são indexados por chaves.
Dicionários são criados com chaves {} ou a função dict().

dicionario = {'chave': 'valor'}
dict(chave='valor')
pessoa = {
    'nome': 'Vitor',
    'sobrenome': 'Hugo',
    'idade': 24,
    'altura': 1.83,
    'peso': 67,
    'endereco': [
        {'Rua': 'Rua 1', 'Numero': 123},
        {'Rua': 'Rua 2', 'Numero': 456}
    ]
}

Metodos uteis para dicionarios:
pessoa.keys() -> Retorna uma lista com as chaves do dicionario
pessoa.values() -> Retorna uma lista com os valores do dicionario
pessoa.items() -> Retorna uma lista com tuplas contendo chave e valor
pessoa.get('nome') -> Retorna o valor da chave 'nome'
pessoa.__len__() ou len(pessoa) -> Retorna o tamanho do dicionario
pessoa.setdefault('email', ' ') -> Retorna o valor da chave 'email' ou cria a chave com o valor ' '
pessoa.copy() -> Retorna uma copia do dicionario
pessoa.clear() -> Limpa o dicionario
pessoa.pop('nome') -> Remove a chave 'nome' do dicionario
pessoa.popitem() -> Remove a ultima chave adicionada no dicionario
pessoa.update({'nome': 'Vitor Hugo'}) -> Atualiza o valor da chave 'nome' para 'Vitor Hugo'
pessoa.fromkeys(['nome', 'sobrenome'], ' ') -> Cria um dicionario com as chaves 'nome' e 'sobrenome' e o valor ' '

"""

#Sets (Conjuntos)

"""
Sets são coleções de dados não ordenadas e sem elementos duplicados.
Sets são mutáveis, mas seus elementos devem ser imutáveis.
Sets são criados com chaves {} ou a função set().
set1 = {1, 2, 3, 4, 5} ou set2 = set([1, 2, 3, 4, 5])

Metodos uteis para sets:
set1.add(6) -> Adiciona o elemento 6 ao set
set1.remove(6) -> Remove o elemento 6 do set
set1.discard(6) -> Remove o elemento 6 do set, se ele existir
set1.pop() -> Remove um elemento aleatório do set
set1.clear() -> Limpa o set

set1.union(set2) ou set1 | set2 -> Retorna a união de set1 e set2
set1.intersection(set2) ou set1 & set2 -> Retorna a interseção de set1 e set2
set1.difference(set2) ou set1 - set2 -> Retorna a diferença de set1 e set2
set1.symmetric_difference(set2) ou set1 ^ set2 -> Retorna a diferença simétrica de set1 e set2


Sets são usados para remover duplicatas de uma lista e realizar operações de conjuntos.
- eles não são indexados
- seus valores são únicos
- não garantem a ordem dos elementos
- são interaveis com for, in, not in
"""

#lambda
"""
Lambda é uma função anônima definida com a palavra-chave lambda.
Lambda é usada para criar funções simples e de uma linha.
Lambda é uma expressão, não uma declaração.
lambda argumentos: expressão
l1 = sorted(array, key=lambda x: x[1]) -> Ordena a lista array com base no segundo elemento de cada sublista
"""
# Exemplo 1: Filtrar uma lista de números para obter apenas os pares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]

# Exemplo 2: Ordenar uma lista de tuplas pelo segundo elemento
tuplas = [(1, 'um'), (2, 'dois'), (3, 'tres'), (4, 'quatro')]
ordenado = sorted(tuplas, key=lambda x: x[1])
print(ordenado)  # Saída: [(4, 'quatro'), (2, 'dois'), (3, 'tres'), (1, 'um')]

lambda x, y: x + y  # Função lambda que soma dois números

#_______________________________________________________________________________________________________________________

#list comprehension
"""
List comprehension é uma forma concisa de criar listas em Python.
List comprehension é mais eficiente que loops tradicionais.
List comprehension é uma expressão, não uma declaração.
lista = [n ** 2 for n in range(10)] -> Cria uma lista com os quadrados dos números de 0 a 9
Podemos usar if e else em list comprehension para filtrar elementos.
lista = [n if n % 2 == 0 else 'impar' for n in range(10)] -> Cria uma lista com números pares e 'impar' para ímpares
set = {n ** 2 for n in range(10)} -> Cria um set com os quadrados dos números de 0 a 9
"""

#isinstance
"""
isinstance é uma função que verifica se um objeto é de um determinado tipo.
isinstance(objeto, tipo)
isinstance(10, int) -> True
isinstance('texto', str) -> True
isinstance([1, 2, 3], list) -> True

"""

#hasttr
"""
hasattr -> Verifica se um objeto possui um atributo
hasattr(objeto, 'atributo')
"""

#interable e iterator
"""
Iterable é um objeto que pode ser iterado.
Iterator é um objeto que mantém o estado durante a iteração.
iter() -> Converte um objeto iterável em um iterator
next() -> Retorna o próximo elemento de um iterator
__iter__() -> Método que retorna um iterator
__next__() -> Método que retorna o próximo elemento de um iterator

"""