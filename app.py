from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn
from secrets import token_hex
import os
from dotenv import load_dotenv
import services.database as db
import frontend.CustomAPI as custom_api
from models.schemas import CreateTableRequest, CreateTableResponse, InsertIntoTableRequest, InsertIntoTableResponse, ListTablesResponse, SelectFromTableRequest, SelectFromTableResponse, UpdateTableRequest, UpdateTableResponse, DeleteFromTableRequest, DeleteFromTableResponse



db_service = db.Database()
db_service.connect_db()

'''
# Criação do app FastAPI
app = FastAPI(title = "⚡ API Banco de Dados",
              description = "Funcionalidades para manipulação de banco de dados.",
              contact = 
              {
                  "name": "Rogério Gravina",
                  "url": "https:https://gitlab.cade.gov.br/rogerio.gravina/",
                  "email": "rogerio.gravina@cade.gov.br"
                  },
                version = "1.0.0",
                redoc_url="/intro", 
              )

'''
app = FastAPI(redoc_url= "/intro")

custom_api_dict = custom_api.custom_api()

@app.on_event("startup")
async def startup_event():
    app.openapi_schema = custom_api_dict


# Rota raiz redireciona para /docs
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/intro")




# Rotas


#Criar tabela
@app.post("/create_table_from_dict/")
def create_table(request: CreateTableRequest) -> CreateTableResponse:
    """
    Cria uma tabela no banco de dados.

    - **nome_da_tabela**: Nome da tabela a ser criada.
    <br>
    <br>
    - **colunas**: Dicionário contendo as colunas e seus tipos.
     <br> - _Exemplo_:
                {
                    "id": "INT",
                    "nome": "VARCHAR(100)",
                    "email": "VARCHAR(100)"
                }
    O campo "id" é obrigatório e deve ser do tipo "INT" ou "BIGINT".
    Ele é a chave primária da tabela e será autoincrementado.
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    # Criar a string de criação da tabela
    db_service.create_table_from_dict(
        table_name=request.nome_da_tabela, fields=request.colunas
    )
    return {
        "mensagem": "Tabela criada com sucesso!",
        "banco_de_dados": str(name),
        "nome_da_tabela": str(request.nome_da_tabela),
        "colunas": str(request.colunas),
    }






# Inserir dados em uma tabela
@app.post("/insert_into_table_from_dict/")
def insert_into_table(request: InsertIntoTableRequest) -> InsertIntoTableResponse:
    """
    Insere dados em uma tabela.

    - **nome_da_tabela**: Nome da tabela a ser criada.
    <br>
    <br>
    - **valores***: Dicionário contendo os valores a serem inseridos na tabela.
     <br> - _Exemplo_:
                {
                    "nome": "Cade",
                    "email": "cade@cade.gov.br"
                    }
    <br>
    <br>
    *Se a tabela possuir o campo 'id', ele não precisa ser fornecido, pois é a chave primária da tabela e será autoincrementado.
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    # Criar a string de inserção de dados
    db_service.insert_into_table_from_dict(
        table_name=request.nome_da_tabela, fields=request.valores
    )
    return {
        "mensagem": "Dados inseridos com sucesso!",
        "banco_de_dados": str(name),
        "nome_da_tabela": str(request.nome_da_tabela),
        "valores": str(request.valores),
    }





# Selecionar dados de uma tabela
@app.post("/select_from_table/")
def select_from_table(request: SelectFromTableRequest) -> SelectFromTableResponse:
    """
    Seleciona dados de uma tabela.

    - **nome_da_tabela**: Nome da tabela a ser solicitado os dados.
    <br>
    <br>
    - **colunas**: Lista contendo os nomes das colunas a serem selecionadas.
     <br> - _Exemplo_:
                [
                    "nome",
                    "email"
                ]
    <br>
    <br>
    - **where**: String contendo a condição de seleção dos dados.
     <br> - _Exemplo_:
                "nome = 'Cade'"
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    # Criar a string de seleção de dados
    result = db_service.select_from_table(
        table_name=request.nome_da_tabela, fields=request.colunas, where=request.where
    )

    result = [list(row) for row in result]
    return {
        "nome_da_tabela": str(request.nome_da_tabela),
        "resultado": str(result),
    }






# Atualizar dados de uma tabela
@app.post("/update_table_from_dict/")
def update_table(request: UpdateTableRequest) -> UpdateTableResponse:
    """
    Atualiza dados de uma tabela.

    - **nome_da_tabela**: Nome da tabela a ser atualizada.
    <br>
    <br>
    - **valores**: Dicionário contendo os valores a serem atualizados na tabela.
     <br> - _Exemplo_:
                {
                    "nome": "Cade",
                    "email": "cade@cade.gov.br"
                    }
    <br>
    <br>
    - **where**: String contendo a condição de atualização dos dados.
     <br> - _Exemplo_:
                "nome = 'Cade'"
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    # Criar a string de atualização de dados
    db_service.update_table_from_dict(
        table_name=request.nome_da_tabela, fields=request.valores, where=request.where
    )
    return {
        "mensagem": "Dados atualizados com sucesso!",
        "banco_de_dados": str(name),
        "nome_da_tabela": str(request.nome_da_tabela),
        "valores_inseridos": str(request.valores),
    }






# Deletar dados de uma tabela
@app.post("/delete_from_table/")
def delete_from_table(request: DeleteFromTableRequest) -> DeleteFromTableResponse:
    """
    Deleta dados de uma tabela.

    - **nome_da_tabela**: Nome da tabela a ser deletada.
    <br>
    <br>
    - **where**: String contendo a condição de deleção dos dados.
     <br> - _Exemplo_:
                "nome = 'Cade'"
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    # Criar a string de deleção de dados
    db_service.delete_from_table(
        table_name=request.nome_da_tabela, where=request.where
    )
    return {
        "mensagem": "Dados deletados com sucesso!",
        "banco_de_dados": str(name),
        "nome_da_tabela": str(request.nome_da_tabela),
        "valores_deletados": str(request.where),
    }






# Listar tabelas existentes
@app.get("/list_tables/")
def list_tables() -> ListTablesResponse:
    """
    Lista as tabelas do banco de dados.

    Retorna uma lista de tuplas contendo o nome das tabelas.
    """

    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()").fetchone()[0]

    table_names_raw = db_service.list_tables()
    table_names = [table_name[0] for table_name in table_names_raw]
    table_dict = {}
    for i in range(len(table_names)):
        table_dict['Schema ' + str(i+1)] = table_names[i]

    return {
        "banco_de_dados": str(name),
        "tabelas": str(table_dict),
    }







if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)