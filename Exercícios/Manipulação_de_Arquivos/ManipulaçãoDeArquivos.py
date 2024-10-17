# Cria um arquivo txt e escreve uma mensagem nele

arquivo_txt = 'novo_arquivo.txt'

#Abre e fecha o arquivo em modo de escrita
with open(arquivo_txt, 'w') as arquivo:
    arquivo.write('teste1')
print(f'Arquivo {arquivo_txt} criado com sucesso.')

with open(arquivo_txt, 'r') as arquivo:
    print(arquivo.read())

#Abre e fecha o arquivo em modo de adição e corrige os caracteres com acento
with open(arquivo_txt, 'a', encoding='UTF-8') as arquivo:
    arquivo.write('Atenção /n')