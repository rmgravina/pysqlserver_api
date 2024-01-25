import pyodbc
import os
import configparser
import sqlite3

# Considerar remover a escolha entre sqlite3 e SQL Server (As querys são diferentes)
class Database:

    def __init__(self, config_file='.cfg'):
        # Criar um objeto ConfigParser
        self.config = configparser.ConfigParser()

        # Ler as configurações do arquivo .cfg
        # Use a variável para armazenar o resultado da leitura e verificar posteriormente
        config_read = self.config.read(config_file)
        
        # Verificar se o arquivo foi lido com sucesso
        if not config_read:
            raise FileNotFoundError(f"Arquivo {config_file} não encontrado ou não pôde ser lido.")
        
        self.cursor = None
        self.conn = None

    def connect_db(self):
        db_type = self.config.get('database', 'DB_TYPE')
        # Verificar o tipo de banco de dados
        if db_type.lower() == 'sqlite3':

            # Configurações para SQLite3
            sqlite_db_file = self.config.get('database', 'SQLITE_DB_FILE')
            self.conn = sqlite3.connect(sqlite_db_file)
            self.cursor = self.conn.cursor()

        else:

            # Configurações para SQL Server
            driver = self.config.get('database', 'DRIVER')
            server = self.config.get('database', 'SERVER')
            database = self.config.get('database', 'DATABASE')
            uid = self.config.get('database', 'UID')
            pwd = self.config.get('database', 'PWD')
            conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={uid};PWD={pwd};'
            self.conn = pyodbc.connect(conn_str)
            self.cursor = self.conn.cursor()






    def create_table_from_dict(self, table_name: str, fields: dict):
        # Verificar se há um campo "id" na definição da tabela
        if 'id' not in fields:
            print("Erro: A chave 'id' é obrigatória na definição da tabela.")
            return
        
        # Criar a string de criação da tabela
        sql = f'CREATE TABLE {table_name} ('
        for field_name, field_type in fields.items():
            if field_name == 'id':
                sql += f'{field_name} {field_type} IDENTITY(1,1) PRIMARY KEY,'
            else:
                sql += f'{field_name} {field_type},'
        sql = sql[:-1] + ')'  # Remover a última vírgula e adicionar o parêntese de fechamento

        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()

    

    def list_tables(self):

        # Criar a string de listagem de tabelas
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"

        # Executar o comando SQL
        self.cursor.execute(sql)

        # Retornar o resultado
        return self.cursor.fetchall()
    



    def insert_into_table_from_dict(self, table_name: str, fields: dict):
        
        # Criar a string de inserção de dados
        sql = f'INSERT INTO {table_name} ('
        for field_name in fields.keys():
            sql += f'{field_name},'
        sql = sql[:-1] + ') VALUES ('
        for field_value in fields.values():
            sql += f"'{field_value}',"
        sql = sql[:-1] + ')'

        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()
    



    def select_from_table(self, table_name: str, fields: list, where: str = None):
        
        # Criar a string de seleção de dados
        sql = f'SELECT '
        for field in fields:
            sql += f'{field},'
        sql = sql[:-1] + f' FROM {table_name}'
        if where:
            sql += f' WHERE {where}'

        # Executar o comando SQL
        self.cursor.execute(sql)

        # Retornar o resultado
        return self.cursor.fetchall()




    def update_table_from_dict(self, table_name: str, fields: dict, where: str = None):
        
        # Criar a string de atualização de dados
        sql = f'UPDATE {table_name} SET '
        for field_name, field_value in fields.items():
            sql += f'{field_name} = \'{field_value}\','
        sql = sql[:-1]
        if where:
            sql += f' WHERE {where}'

        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()
    



    def delete_from_table(self, table_name: str, where: str = None):
        
        # Criar a string de exclusão de dados
        sql = f'DELETE FROM {table_name}'
        if where:
            sql += f' WHERE {where}'

        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()