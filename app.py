from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn
from secrets import token_hex
import os
from dotenv import load_dotenv
import services.database as db



load_dotenv()

db_service = db.Database()
db_service.connect_db()



# Modelo Pydantic para a entrada da rota create_table_from_dict
class CreateTableRequest(BaseModel):
    nome_da_tabela: str
    colunas: dict


# Modelo Pydantic para a resposta da rota create_table_from_dict
class CreateTableResponse(BaseModel):
    mensagem: str
    banco_de_dados: str
    nome_da_tabela: str
    colunas: str



# Criação do app FastAPI
app = FastAPI(title=os.getenv('TITLE'), description=os.getenv('DESCRIPTION'))



# Rota raiz redireciona para /docs
@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")



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

    Retorna uma mensagem de sucesso e informações sobre a tabela criada.
    """
    # Identificar o banco de dados
    name = db_service.cursor.execute("SELECT DB_NAME()")
    name = name.fetchone()[0]

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


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)








'''
# Rota para escrita de formulário (from list of tuples)
@app.post("/create_table/")
def create_table(table_name, fields: str):
    
    db_service.create_table(table_name=table_name, fields=eval(fields))
    return {"message": "Formulário enviado com sucesso!",
            "table_name": str(table_name),
            "fields": str(fields)}
'''






'''

Ultima alteração: 23/01/2024

    * Verificar como subir a API

'''