from pydantic import BaseModel


# Modelo Pydantic para a entrada e saída da rota create_table_from_dict
class CreateTableRequest(BaseModel):
    nome_da_tabela: str
    colunas: dict

class CreateTableResponse(BaseModel):
    mensagem: str
    banco_de_dados: str
    nome_da_tabela: str
    colunas: str




# Modelo Pydantic para a entrada e saída da rota insert_into_table_from_dict
class InsertIntoTableRequest(BaseModel):
    nome_da_tabela: str
    valores: dict

class InsertIntoTableResponse(BaseModel):
    mensagem: str
    banco_de_dados: str
    nome_da_tabela: str
    valores: str




# Modelo Pydantic para a resposta da rota list_tables
class ListTablesResponse(BaseModel):
    banco_de_dados: str
    tabelas: str




# Modelo Pydantic para a entrada e saída da rota select_from_table
class SelectFromTableRequest(BaseModel):
    nome_da_tabela: str
    colunas: list
    where: str = None

class SelectFromTableResponse(BaseModel):
    nome_da_tabela: str
    resultado: str





# Modelo Pydantic para a entrada e saída da rota update_table_from_dict
class UpdateTableRequest(BaseModel):
    nome_da_tabela: str
    valores: dict
    where: str = None

class UpdateTableResponse(BaseModel):
    mensagem: str
    banco_de_dados: str
    nome_da_tabela: str
    valores_inseridos: str





# Modelo Pydantic para a entrada e saída da rota delete_from_table
class DeleteFromTableRequest(BaseModel):
    nome_da_tabela: str
    where: str = None

class DeleteFromTableResponse(BaseModel):
    mensagem: str
    banco_de_dados: str
    nome_da_tabela: str
    valores_deletados: str