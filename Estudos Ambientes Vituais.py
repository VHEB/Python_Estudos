#Ambiente Virtual
"""
Ambiente Virtual carrega toda a sua instalação do Python
em um diretório isolado, permitindo que você trabalhe em um projeto
sem afetar o ambiente global do Python.
"""
#pip install virtualenv

#virtualenv venv - cria um ambiente virtual

#No terminal, digite:
"""
python -v -> Versão do Python
python -m venv nome_do_ambiente -> Cria um ambiente virtual
cd nome_do_ambiente/Scripts -> Entra no diretório do ambiente virtual
.venv/Scripts/activate -> Ativa o ambiente virtual

pip freeze -> Lista todos os pacotes instalados no ambiente virtual
pip index versions -> Lista todas as versões de um pacote
pip install nome_do_pacote -> Instala um pacote
pip install nome_do_pacote==versão -> Instala uma versão específica de um pacote

deactivate -> Desativa o ambiente virtual
pip uninstall nome_do_pacote -> Desinstala um pacote

pip install -r requirements.txt -> Instala todos os pacotes listados no arquivo requirements.txt
pip freeze > requirements.txt -> Salva todos os pacotes instalados no arquivo requirements.txt

"""

#Criando Arquivos com Python
"""
Modos:
r -> Leitura
w -> Escrita
a -> Adição
r+ -> Leitura e Escrita
w+ -> Escrita e Leitura
a+ -> Adição e Leitura


Metodos Uteis:
write() -> Escreve um texto no arquivo
writeLines() -> Escreve uma lista de texto no arquivo

read() -> Lê o conteúdo do arquivo
readline() -> Lê a primeira linha do arquivo
readlines() -> Lê todas as linhas do arquivo

close() -> Fecha o arquivo
seek() -> Move o cursor para uma posição específica

os.remove() -> Remove um arquivo
os.unlink() -> Remove um arquivo
os.rename() -> Renomeia um arquivo

os.path.exists() -> Verifica se um arquivo existe
os.path.getsize() -> Retorna o tamanho de um arquivo
os.path.is_file() -> Verifica se é um arquivo
os.path.is_dir() -> Verifica se é um diretório


with open('teste.txt', 'w') as arquivo: -> Abre o arquivo e fecha automaticamente

O modo 'b' é utilizado para arquivos binários
O modo 'w' sobrescreve o arquivo
O modo 'a' adiciona ao final do arquivo

"""