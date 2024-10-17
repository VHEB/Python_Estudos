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

