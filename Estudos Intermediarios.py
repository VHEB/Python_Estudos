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