"""
Interpretador do Python

python --version
python --help
python -c "print('Hello World!')"
python mod.py # Executa o arquivo mod.py
python -m mod # Executa o módulo mod
python -u # Modo não bufferizado 
python -i # Modo interativo
python -c 'cmd' # Executa o comando cmd
python -h # Ajuda
python -V # Versão

#_______________________________________________________________________________________________________________________

The Zen of Python, por Tim Peters

Bonito é melhor que feio
Explicito é melhor que implícito
Simples é melhor que complexo
Complexo é melhor que complicado
Plano é melhor que aglomerado
Esparso é melhor que denso
Legibilidade conta
Casos especiais não são especiais o suficiente para quebrar as regras 
Embora a praticidade vença a pureza
Agora é melhor que nunca
Embora nunca frequentemente seja melhor que já
Se a implementação é difícil de explicar, é uma má ideia
Se a implementação é fácil de explicar, pode ser uma boa ideia
Namespaces são uma ótima ideia - vamos fazer mais dessas!
"""




#Parametro Nomeado? 
# Ctrl / para comentar várias linhas
# Letra maiuscula na variável é uma convenção para constantes
# Letra minuscula no inicio da variável é uma convenção são funções e variáveis
# Conversão de tipos, Coerção, typecasting, type conversion, coercion = Conversão de um tipo para outro
#Tabela Unicode -> https://unicode-table.com/pt/
#_______________________________________________________________________________________________________________________

#Funções e Classes Basicas
"""
print("Hello World") -> Função que imprime uma string na tela
input("Digite seu nome: ") -> Função que recebe uma string do usuário

len("Vitor Hugo") -> Função que retorna o tamanho de uma string
in -> Operador que verifica se um valor está presente em uma lista
type(123) -> Função que retorna o tipo de uma variável
id() -> Função que retorna o endereço de memória de uma variável
range(10) -> Função que retorna uma lista de 0 a 9
int("123") -> Função que converte uma string para inteiro
float("123.456") -> Função que converte uma string para float
str(123) -> Função que converte um inteiro para string
enumerate() -> Função que retorna o índice e o valor de uma lista
round(123.456, 2) -> Função que arredonda um número para duas casas decimais

break -> Para a execução do loop
continue -> Pula a execução atual e vai para a próxima
pass -> Não faz nada
breackpoint -> Ponto de parada para debugar o código
"""


#Variáveis
"""
Tipo de tipagem = Dinâmica / Forte
str = string = texto
int = inteiro = 123456 0 -1 -2 -3
float = ponto flutuante = 123.456
bool = booleano = True or False
"""
nome_completo = "Vitor Hugo"
idade_atual = 24
data_nascimento = '16/03/2000'
altura = 1.83
peso = 67
maior_de_idade = idade_atual >= 18
imc = peso / (altura ** 2)
array = [1,2,3,4,5,6,7,8,9,10] #mutavel
dicionario = {'nome': 'Vitor', 'sobrenome': 'Hugo', 'idade': 24} #imutavel | chave: valor | dicionario é uma coleção de dados

#_______________________________________________________________________________________________________________________

#Strings
"""
f-strings -> Formatação de strings -> f"{variável}"
f"{variavel:.2f}" -> Conta com duas casas decimais
format -> Formatação de strings -> "{}".format(variável)

O sep é o separador entre os argumentos passados para a função print
O end é o que será impresso no final da linha
print(1,2,3, sep=' - ', end='\n')

/t -> Tabulação
/n -> Quebra de linha


print("Vitor \"Hugo\" ") # Para imprimir aspas duplas dentro de uma string, é necessário usar a barra invertida
print(r"Vitor \"Hugo\" ") # O r antes da string faz com que a barra invertida seja ignorada
print(type("Vitor Hugo"), type(123456), type(123.456), type(True))

Podemos acessar os caracteres de uma string utilizando colchetes -> string[0]
Podemos acessar um intervalo de caracteres de uma string utilizando colchetes -> string[0:5]
Podemos acessar os caracteres de uma string de trás para frente utilizando colchetes -> string[-1]
Podemos somar strings -> string1 + string2
Podemos multiplicar strings -> string * 3
Podemos verificar se um caractere está presente em uma string -> "a" in string
Podemos verificar se um caractere não está presente em uma string -> "a" not in string
Podemos transformar uma string em uma lista -> list(string)
Interpolação de strings com % -> "%s %d" % (string, inteiro)

replace -> Substitui um valor por outro .replace('valor a ser substituido', 'novo valor')
split -> Separa uma string em uma lista
join -> Junta uma lista em uma string
replace -> Substitui um valor por outro
strip -> Remove espaços em branco
lstrip -> Remove espaços em branco do lado esquerdo
rstrip -> Remove espaços em branco do lado direito
capitalize -> Coloca a primeira letra em maiúsculo
title -> Coloca a primeira letra de cada palavra em maiúsculo
upper -> Coloca todas as letras em maiúsculo
lower -> Coloca todas as letras em minúsculo
swapcase -> Inverte as letras maiúsculas e minúsculas
count -> Conta a quantidade de um valor
find -> Retorna o índice de um valor
rfind -> Retorna o índice de um valor de trás para frente
_______________________________________________________________________________________________________________________

Formatação Basica de Strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda 
< - Direita
^ - Centro 
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a -> !r -> repr() !s -> str() !a -> ascii() 

print('O hexadecimal de 10 é:', hex(10))
print('O binário de 10 é:', bin(10))
print('O octal de 10 é:', oct(10))
print('O hexadecimal de %d é: %08X' % (1050, 1050))

fatiamento de strings -> string[i:f:s] -> i = inicio, f = fim, s = step
nome = "Vitor Hugo Estefano Barbosa"
print(nome[-1:-27:-1]) #tor
"""

#_______________________________________________________________________________________________________________________

#Operadores

"""
Operadores Aritméticos
+ Soma
- Subtração
* Multiplicação
/ Divisão
// Divisão inteira
** Potência
% Resto da divisão

-> Ordem de precedência
1º ()
2º **
3º *, /, //, %
4º +, -
_____________________________________________________

Operadores Relacionais
== Igual
!= Diferente
< Menor que
> Maior que
<= Menor ou igual
>= Maior ou igual
_____________________________________________________

Comparações
&& and
|| or
!= not
_____________________________________________________

Operadores de Atribuição
= Atribuição
+= Adição
-= Subtração
*= Multiplicação
/= Divisão
//= Divisão inteira
**= Potência
%= Resto da divisão
_____________________________________________________

Zero/None/False são considerados False

"""

#_______________________________________________________________________________________________________________________

# Estruturas condicionais

"""
Comparação de valores if, elif, else
if condição:
    bloco de código
elif condição:
    bloco de código
else:
    bloco de código

Repeticão de valores for, while
for valor in range(10):
    bloco de código

while condição:
    bloco de código

"""

#Tratamento de Erros
"""
try: -> Tenta executar o bloco de código
except: -> Caso ocorra um erro, executa o bloco de código
finally: -> Executa o bloco de código independente do resultado
raise -> Lança uma exceção
assert -> Testa se uma condição é verdadeira

"""

#Listas e Tuplas
"""
Metodos de listas -> append, insert, remove, pop, clear, index, count, sort, reverse, copy
    del lista[0] -> Deleta o valor de um índice
    lista.append(x) -> Adiciona um valor ao final da lista
    lista.insert(indice, valor) -> Adiciona um valor em um índice específico
    remove -> Remove um valor específico
    lista.pop() -> Remove o último valor da lista
    clear -> Limpa a lista
    index -> Retorna o índice de um valor
    count -> Retorna a quantidade de um valor
    sort -> Ordena a lista
    reverse -> Inverte a lista
    copy -> Copia a lista
    lista.extend(lista2) -> Adiciona uma lista a outra lista
Metodos de tuplas -> count, index
    count -> Retorna a quantidade de um valor
    index -> Retorna o índice de um valor

listas = [1, '2', 3.0, True, [1,2,3], (1,2,3)] -> Listas podem conter qualquer tipo de dado, e é mutável (pode ser alterada)
tuplas = ('vitor': 1, 'hugo': 2, 'estefano': 3) -> Tuplas podem conter qualquer tipo de dado, e é imutável (não pode ser alterada)

Desempacotamento de listas 
lista, *_ = [1,2,3,4,5,6,7,8,9,10] -> Atribui o primeiro valor a variável lista e o restante a variável _



"""