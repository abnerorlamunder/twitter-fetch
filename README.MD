# Twitter Fetch

Conecta-se a API do Twitter para buscar tweets através de hashtags previamente cadastradas no aplicativo, e exibe-as.

### Prerequisites

-Python versão 3.8.1;
-Django;
-Conta de desenvolvedor na API do Twitter;

### Installing

```
1- Acessar o diretório do seu projeto e execute:
  python -m venv myvenv
2- Ativar o ambiente através da linha de comando:
  ./myvenv/Scripts/activate
3- Instalar os requisitos do projeto:
  pip install -r requirements.txt
4- (CASO A BASE NÃO EXISTA AINDA) Executar migrations
  4.1 - Para criar o banco de dados:
    python manage.py migrate
  4.2 - Criar o super usuário para ter acesso a página de administração
    python manage.py createsuperuser
4- Rodar a aplicação:
  python manage.py runserver
5- Cadastre hashtags, e será listado os tweets filtrados a partir delas

```
z
## Running the tests

Teste para conectar na API e testar se as credenciais estão válidas

```
python manage.py test
```