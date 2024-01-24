import pyodbc
import os
import configparser
import sqlite3


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



    def create_table(self, table_name: str, fields: list):
        
        # Criar a string de criação da tabela
        sql = f'CREATE TABLE {table_name} ('
        for field in fields:
            # Assumindo que cada campo é uma tupla (nome do campo, tipo do campo)
            field_name, field_type = field
            sql += f'{field_name} {field_type},'
        sql = sql[:-1] + ')' # Remover a última vírgula e adicionar o parênteses de fechamento

        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()


    def create_table_from_dict(self, table_name: str, fields: dict):
         
        # Criar a string de criação da tabela
        sql = f'CREATE TABLE {table_name} ('
        for field_name, field_type in fields.items():
            sql += f'{field_name} {field_type},'
        sql = sql[:-1] + ')'  # Remover a última vírgula e adicionar o parêntese de fechamento
    
        # Executar o comando SQL
        self.cursor.execute(sql)
        self.conn.commit()