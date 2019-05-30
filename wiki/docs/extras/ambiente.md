# Ambiente de Desenvolvimento

## Instalação do Python 3.7.3 e do VirtualEnv
Baixe e instale o [Python](https://www.python.org/downloads/) em seu sistema operacional.
No terminal, rode o seguinte comando: ``` pip3 install virtualenv ```

## Rodar a Aplicação
#### Clonar o Projeto
* Entre no [repositório do projeto](https://github.com/ads-unbind/unbind) e escolha uma forma de clonar o repositório:
    * HTTPS: ``` git clone https://github.com/ads-unbind/unbind.git ```
    * SSH: ``` git clone git@github.com:ads-unbind/unbind.git ```

#### Levantar o Ambiente
* No terminal, entre na pasta src/ e siga os passos:<br >
    1) Crie o VirtuelEnv: ``` virtualenv -p python3 venv ```<br >
    1) Levante o VirtualEnv: ``` source venv/bin/activate ```<br >
    2) Instale as dependências: ``` pip install -r requirements.txt ``` <br >
    3) Rode as migrações: ``` ./manage.py migrate ```<br >
    4) Rode o servidor: ``` ./manage.py runserver ```
