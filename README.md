# ⚡ PySQL Server API

<p align="center">
  <img src="frontend\misc\api_logo.jpg" alt="Descrição da imagem">
</p>

- [Descrição](#-descrição)
- [Documentação da API](#-documentação-da-api)
   - [Configurar Banco de Dados](#configurar-banco-de-dados)
   - [Criar Tabela](#criar-tabela)
   - [Inserir Dados](#inserir-dados)
   - [Selecionar Dados](#selecionar-dados)
   - [Atualizar Dados](#atualizar-dados)
   - [Excluir Dados](#excluir-dados)
   - [Listar Tabelas](#listar-tabelas)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Autor](#-autor)
- [Licença](#-licença)


## 📝 Descrição

A PySQL Server API é uma ferramenta para implementar API de operações CRUD em banco de dados SQL Server. Foi desenvolvida em Python utilizando as bibliotecas pyodbc, FastAPI e Uvicorn. Ela oferece funcionalidades para manipulação de bancos de dados, permitindo que os usuários criem tabelas, insiram, selecionem, atualizem e excluam dados nas tabelas.

## 🔍 Documentação da API

A documentação completa da API pode ser encontrada na rota `/intro` do Swagger. Aqui estão os principais endpoints disponíveis:

### Configurar Banco de Dados

Renomeie o arquivo `EXAMPLE.cfg` para `.cfg` e preencha os campos com as informações do seu banco de dados.

### Criar Tabela

- Método: `POST`
- Rota: `/create_table_from_dict/`
- Descrição: Cria uma tabela no banco de dados.
- Parâmetros:
  - **nome_da_tabela**: Nome da tabela a ser criada.
  - **colunas**: Dicionário contendo as colunas e seus tipos.
    - Exemplo:
      ```json
      {
        "id": "INT",
        "nome": "VARCHAR(100)",
        "email": "VARCHAR(100)"
      }
      ```
      O campo "id" é obrigatório e deve ser do tipo "INT" ou "BIGINT". Ele é a chave primária da tabela e será autoincrementado.
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/create_table_from_dict/'
  body = {
      'nome_da_tabela': 'example_table',
      'colunas': {
          'id': 'INT',
          'nome': 'VARCHAR(100)',
          'email': 'VARCHAR(100)'
      }
  }
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, json=body, headers=headers)
  print(response.json())
  ```

### Inserir Dados

- Método: `POST`
- Rota: `/insert_into_table_from_dict/`
- Descrição: Insere dados em uma tabela.
- Parâmetros:
  - **nome_da_tabela**: Nome da tabela em que os dados serão inseridos.
  - **valores**: Dicionário contendo os valores a serem inseridos na tabela.
    - Exemplo:
      ```json
      {
        "nome": "username",
        "email": "username@domain.com.br"
      }
      ```
      Se a tabela possuir o campo 'id', ele não precisa ser fornecido, pois é a chave primária da tabela e será autoincrementado.
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/insert_into_table_from_dict/'
  body = {
      'nome_da_tabela': 'example_table',
      'valores': {
          'nome': 'username',
          'email': 'username@domain.com.br'
      }
  }
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, json=body, headers=headers)
  print(response.json())
  ```

### Selecionar Dados

- Método: `POST`
- Rota: `/select_from_table/`
- Descrição: Seleciona dados de uma tabela.
- Parâmetros:
  - **nome_da_tabela**: Nome da tabela em que os dados serão selecionados.
  - **colunas**: Lista contendo os nomes das colunas a serem selecionadas.
    - Exemplo:
      ```json
      [
        "nome",
        "email"
      ]
      ```
  - **where**: String contendo a condição de seleção dos dados.
    - Exemplo:
      `"nome = 'username'"`
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/select_from_table/'
  body = {
      'nome_da_tabela': 'example_table',
      'colunas': ['nome', 'email'],
      'where': "nome = 'username'"
  }
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, json=body, headers=headers)
  print(response.json())
  ```

### Atualizar Dados

- Método: `POST`
- Rota: `/update_table_from_dict/`
- Descrição: Atualiza dados de uma tabela.
- Parâmetros:
  - **nome_da_tabela**: Nome da tabela em que os dados serão atualizados.
  - **valores**: Dicionário contendo os valores a serem atualizados na tabela.
    - Exemplo:
      ```json
      {
        "nome": "username",
        "email": "username@domain.com.br"
      }
      ```
  - **where**: String contendo a condição de atualização dos dados.
    - Exemplo:
      `"nome = 'username'"`
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/update_table_from_dict/'
  body = {
      'nome_da_tabela': 'example_table',
      'valores': {
          'nome': 'username',
          'email': 'username@domain.com.br'
      },
      'where': "nome = 'username'"
  }
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, json=body, headers=headers)
  print(response.json())
  ```

### Excluir Dados

- Método: `POST`
- Rota: `/delete_from_table/`
- Descrição: Deleta dados de uma tabela.
- Parâmetros:
  - **nome_da_tabela**: Nome da tabela em que os dados serão deletados.
  - **where**: String contendo a condição de deleção dos dados.
    - Exemplo:
      `"nome = 'username'"`
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/delete_from_table/'
  body = {
      'nome_da_tabela': 'example_table',
      'where': "nome = 'username'"
  }
  headers = {'Content-Type': 'application/json'}
  response = requests.post(url, json=body, headers=headers)
  print(response.json())
  ```

### Listar Tabelas

- Método: `GET`
- Rota: `/list_tables/`
- Descrição: Lista as tabelas do banco de dados.
- Exemplo de Requisição (Python):
  ```python
  import requests

  url = 'https://example.com/list_tables/'
  response = requests.get(url)
  print(response.json())
  ```

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn

## 🎯 Autor

- Nome: Rogério Gravina
- GitLab: [rogerio.gravina](https://https//gitlab.cade.gov.br/rogerio.gravina/)
- Email: rogerio.gravina@cade.gov.br

## 📚 Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/license/mit/).