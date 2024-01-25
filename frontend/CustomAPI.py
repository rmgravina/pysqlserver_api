from fastapi import FastAPI
import os

def custom_api():

    custom_api = {
    "openapi": "3.1.0",
    "info": {
        "title": "⚡ API Banco de Dados",
        "x-logo": {
                "url": "https://i.ibb.co/0n3z3Cf/api-logo.jpg",
                },
        "description": "Funcionalidades para manipulação de banco de dados.",
        "contact": {
            "name": "Rogério Gravina",
            "url": "https://https//gitlab.cade.gov.br/rogerio.gravina/",
            "email": "rogerio.gravina@cade.gov.br"
        },
        "version": "1.0.0"
    },
    "paths": {
        "/create_table_from_dict/": {
            "post": {
                "summary": "Criar Tabela ✨",
                "description": "Cria uma tabela no banco de dados.\n\n- **nome_da_tabela**: Nome da tabela a ser criada.\n<br>\n<br>\n- **colunas**: Dicionário contendo as colunas e seus tipos.\n <br> - _Exemplo_:\n            {\n                \"id\": \"INT\",\n                \"nome\": \"VARCHAR(100)\",\n                \"email\": \"VARCHAR(100)\"\n            }\nO campo \"id\" é obrigatório e deve ser do tipo \"INT\" ou \"BIGINT\".\nEle é a chave primária da tabela e será autoincrementado.",
                "operationId": "create_table_create_table_from_dict__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/CreateTableRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/CreateTableResponse"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
                {
                    "lang": "Python 🐍",
                    "source": "import requests\n\nurl = 'https://example.com/create_table_from_dict/'\nbody = {\n    'nome_da_tabela': 'example_table',\n    'colunas': {\n        'id': 'INT',\n        'nome': 'VARCHAR(100)',\n        'email': 'VARCHAR(100)'\n    }\n}\nheaders = {'Content-Type': 'application/json'}\nresponse = requests.post(url, json=body, headers=headers)\nprint(response.json())"
                },
                {
                    "lang": "JavaScript 🟨",
                    "source": "const url = 'https://example.com/create_table_from_dict/';\nconst body = {\n    nome_da_tabela: 'example_table',\n    colunas: {\n        id: 'INT',\n        nome: 'VARCHAR(100)',\n        email: 'VARCHAR(100)'\n    }\n};\nconst headers = { 'Content-Type': 'application/json' };\n\nfetch(url, {\n    method: 'POST',\n    headers: headers,\n    body: JSON.stringify(body)\n})\n    .then(response => response.json())\n    .then(data => console.log(data));"
                }
            ]
        }
        },
        "/insert_into_table_from_dict/": {
            "post": {
                "summary": "Inserir dados 📝",
                "description": "Insere dados em uma tabela.\n\n- **nome_da_tabela**: Nome da tabela a ser criada.\n<br>\n<br>\n- **valores***: Dicionário contendo os valores a serem inseridos na tabela.\n <br> - _Exemplo_:\n            {\n                \"nome\": \"Cade\",\n                \"email\": \"cade@cade.gov.br\"\n                }\n<br>\n<br>\n*Se a tabela possuir o campo 'id', ele não precisa ser fornecido, pois é a chave primária da tabela e será autoincrementado.",
                "operationId": "insert_into_table_insert_into_table_from_dict__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/InsertIntoTableRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/InsertIntoTableResponse"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
            {
                "lang": "Python 🐍",
                "source": "import requests\n\nurl = 'https://example.com/insert_into_table_from_dict/'\nbody = {\n    'nome_da_tabela': 'example_table',\n    'valores': {\n        'nome': 'Cade',\n        'email': 'cade@cade.gov.br'\n    }\n}\nheaders = {'Content-Type': 'application/json'}\nresponse = requests.post(url, json=body, headers=headers)\nprint(response.json())"
            },
            {
                "lang": "JavaScript 🟨",
                "source": "const url = 'https://example.com/insert_into_table_from_dict/';\nconst body = {\n    nome_da_tabela: 'example_table',\n    valores: {\n        nome: 'Cade',\n        email: 'cade@cade.gov.br'\n    }\n};\nconst headers = { 'Content-Type': 'application/json' };\n\nfetch(url, {\n    method: 'POST',\n    headers: headers,\n    body: JSON.stringify(body)\n})\n    .then(response => response.json())\n    .then(data => console.log(data));"
            }
            ]
        }
        },
        "/select_from_table/": {
            "post": {
                "summary": "Selecionar dados 🔍",
                "description": "Seleciona dados de uma tabela.\n\n- **nome_da_tabela**: Nome da tabela a ser solicitado os dados.\n<br>\n<br>\n- **colunas**: Lista contendo os nomes das colunas a serem selecionadas.\n <br> - _Exemplo_:\n            [\n                \"nome\",\n                \"email\"\n            ]\n<br>\n<br>\n- **where**: String contendo a condição de seleção dos dados.\n <br> - _Exemplo_:\n            \"nome = 'Cade'\"",
                "operationId": "select_from_table_select_from_table__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/SelectFromTableRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/SelectFromTableResponse"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
            {
                "lang": "Python 🐍",
                "source": "import requests\n\nurl = 'https://example.com/select_from_table/'\nbody = {\n    'nome_da_tabela': 'example_table',\n    'colunas': ['nome', 'email'],\n    'where': \"nome = 'Cade'\"\n}\nheaders = {'Content-Type': 'application/json'}\nresponse = requests.post(url, json=body, headers=headers)\nprint(response.json())"
            },
            {
                "lang": "JavaScript 🟨",
                "source": "const url = 'https://example.com/select_from_table/';\nconst body = {\n    nome_da_tabela: 'example_table',\n    colunas: ['nome', 'email'],\n    where: \"nome = 'Cade'\"\n};\nconst headers = { 'Content-Type': 'application/json' };\n\nfetch(url, {\n    method: 'POST',\n    headers: headers,\n    body: JSON.stringify(body)\n})\n    .then(response => response.json())\n    .then(data => console.log(data));"
            }
            ],
        }
        },
        "/update_table_from_dict/": {
            "post": {
                "summary": "Atualizar dados 🔁",
                "description": "Atualiza dados de uma tabela.\n\n- **nome_da_tabela**: Nome da tabela a ser atualizada.\n<br>\n<br>\n- **valores**: Dicionário contendo os valores a serem atualizados na tabela.\n <br> - _Exemplo_:\n            {\n                \"nome\": \"Cade\",\n                \"email\": \"cade@cade.gov.br\"\n                }\n<br>\n<br>\n- **where**: String contendo a condição de atualização dos dados.\n <br> - _Exemplo_:\n            \"nome = 'Cade'\"",
                "operationId": "update_table_update_table_from_dict__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/UpdateTableRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/UpdateTableResponse"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
            {
                "lang": "Python 🐍",
                "source": "import requests\n\nurl = 'https://example.com/update_table_from_dict/'\nbody = {\n    'nome_da_tabela': 'example_table',\n    'valores': {\n        'nome': 'Cade',\n        'email': 'cade@cade.gov.br'\n    },\n    'where': \"nome = 'Cade'\"\n}\nheaders = {'Content-Type': 'application/json'}\nresponse = requests.post(url, json=body, headers=headers)\nprint(response.json())"
            },
            {
                "lang": "JavaScript 🟨",
                "source": "const url = 'https://example.com/update_table_from_dict/';\nconst body = {\n    nome_da_tabela: 'example_table',\n    valores: {\n        nome: 'Cade',\n        email: 'cade@cade.gov.br'\n    },\n    where: \"nome = 'Cade'\"\n};\nconst headers = { 'Content-Type': 'application/json' };\n\nfetch(url, {\n    method: 'POST',\n    headers: headers,\n    body: JSON.stringify(body)\n})\n    .then(response => response.json())\n    .then(data => console.log(data));"
            }
            ],
        }
        },
        "/delete_from_table/": {
            "post": {
                "summary": "Excluir dados 🔥",
                "description": "Deleta dados de uma tabela.\n\n- **nome_da_tabela**: Nome da tabela a ser deletada.\n<br>\n<br>\n- **where**: String contendo a condição de deleção dos dados.\n <br> - _Exemplo_:\n            \"nome = 'Cade'\"",
                "operationId": "delete_from_table_delete_from_table__post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/DeleteFromTableRequest"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/DeleteFromTableResponse"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
            {
                "lang": "Python 🐍",
                "source": "import requests\n\nurl = 'https://example.com/delete_from_table/'\nbody = {\n    'nome_da_tabela': 'example_table',\n    'where': \"nome = 'Cade'\"\n}\nheaders = {'Content-Type': 'application/json'}\nresponse = requests.post(url, json=body, headers=headers)\nprint(response.json())"
            },
            {
                "lang": "JavaScript 🟨",
                "source": "const url = 'https://example.com/delete_from_table/';\nconst body = {\n    nome_da_tabela: 'example_table',\n    where: \"nome = 'Cade'\"\n};\nconst headers = { 'Content-Type': 'application/json' };\n\nfetch(url, {\n    method: 'POST',\n    headers: headers,\n    body: JSON.stringify(body)\n})\n    .then(response => response.json())\n    .then(data => console.log(data));"
            }
            ],
        }
        },
        "/list_tables/": {
            "get": {
                "summary": "Listar Tabelas 🧮",
                "description": "Lista as tabelas do banco de dados.\n\nRetorna uma lista de tuplas contendo o nome das tabelas.",
                "operationId": "list_tables_list_tables__get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/ListTablesResponse"
                                }
                            }
                        }
                    }
                },
                "x-codeSamples": [
            {
                "lang": "Python 🐍",
                "source": "import requests\n\nurl = 'https://example.com/list_tables/'\nresponse = requests.get(url)\nprint(response.json())"
            },
            {
                "lang": "JavaScript 🟨",
                "source": "const url = 'https://example.com/list_tables/';\n\nfetch(url)\n    .then(response => response.json())\n    .then(data => console.log(data));"
            }
            ],
        }
    }
    },
    "components": {
        "schemas": {
            "CreateTableRequest": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "colunas": {
                        "type": "object",
                        "title": "Colunas"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela",
                    "colunas"
                ],
                "title": "CreateTableRequest"
            },
            "CreateTableResponse": {
                "properties": {
                    "mensagem": {
                        "type": "string",
                        "title": "Mensagem"
                    },
                    "banco_de_dados": {
                        "type": "string",
                        "title": "Banco De Dados"
                    },
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "colunas": {
                        "type": "string",
                        "title": "Colunas"
                    }
                },
                "type": "object",
                "required": [
                    "mensagem",
                    "banco_de_dados",
                    "nome_da_tabela",
                    "colunas"
                ],
                "title": "CreateTableResponse"
            },
            "DeleteFromTableRequest": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "where": {
                        "type": "string",
                        "title": "Where"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela"
                ],
                "title": "DeleteFromTableRequest"
            },
            "DeleteFromTableResponse": {
                "properties": {
                    "mensagem": {
                        "type": "string",
                        "title": "Mensagem"
                    },
                    "banco_de_dados": {
                        "type": "string",
                        "title": "Banco De Dados"
                    },
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "valores_deletados": {
                        "type": "string",
                        "title": "Valores Deletados"
                    }
                },
                "type": "object",
                "required": [
                    "mensagem",
                    "banco_de_dados",
                    "nome_da_tabela",
                    "valores_deletados"
                ],
                "title": "DeleteFromTableResponse"
            },
            "HTTPValidationError": {
                "properties": {
                    "detail": {
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        },
                        "type": "array",
                        "title": "Detail"
                    }
                },
                "type": "object",
                "title": "HTTPValidationError"
            },
            "InsertIntoTableRequest": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "valores": {
                        "type": "object",
                        "title": "Valores"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela",
                    "valores"
                ],
                "title": "InsertIntoTableRequest"
            },
            "InsertIntoTableResponse": {
                "properties": {
                    "mensagem": {
                        "type": "string",
                        "title": "Mensagem"
                    },
                    "banco_de_dados": {
                        "type": "string",
                        "title": "Banco De Dados"
                    },
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "valores": {
                        "type": "string",
                        "title": "Valores"
                    }
                },
                "type": "object",
                "required": [
                    "mensagem",
                    "banco_de_dados",
                    "nome_da_tabela",
                    "valores"
                ],
                "title": "InsertIntoTableResponse"
            },
            "ListTablesResponse": {
                "properties": {
                    "banco_de_dados": {
                        "type": "string",
                        "title": "Banco De Dados"
                    },
                    "tabelas": {
                        "type": "string",
                        "title": "Tabelas"
                    }
                },
                "type": "object",
                "required": [
                    "banco_de_dados",
                    "tabelas"
                ],
                "title": "ListTablesResponse"
            },
            "SelectFromTableRequest": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "colunas": {
                        "items": {},
                        "type": "array",
                        "title": "Colunas"
                    },
                    "where": {
                        "type": "string",
                        "title": "Where"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela",
                    "colunas"
                ],
                "title": "SelectFromTableRequest"
            },
            "SelectFromTableResponse": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "resultado": {
                        "type": "string",
                        "title": "Resultado"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela",
                    "resultado"
                ],
                "title": "SelectFromTableResponse"
            },
            "UpdateTableRequest": {
                "properties": {
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "valores": {
                        "type": "object",
                        "title": "Valores"
                    },
                    "where": {
                        "type": "string",
                        "title": "Where"
                    }
                },
                "type": "object",
                "required": [
                    "nome_da_tabela",
                    "valores"
                ],
                "title": "UpdateTableRequest"
            },
            "UpdateTableResponse": {
                "properties": {
                    "mensagem": {
                        "type": "string",
                        "title": "Mensagem"
                    },
                    "banco_de_dados": {
                        "type": "string",
                        "title": "Banco De Dados"
                    },
                    "nome_da_tabela": {
                        "type": "string",
                        "title": "Nome Da Tabela"
                    },
                    "valores_inseridos": {
                        "type": "string",
                        "title": "Valores Inseridos"
                    }
                },
                "type": "object",
                "required": [
                    "mensagem",
                    "banco_de_dados",
                    "nome_da_tabela",
                    "valores_inseridos"
                ],
                "title": "UpdateTableResponse"
            },
            "ValidationError": {
                "properties": {
                    "loc": {
                        "items": {
                            "anyOf": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "integer"
                                }
                            ]
                        },
                        "type": "array",
                        "title": "Location"
                    },
                    "msg": {
                        "type": "string",
                        "title": "Message"
                    },
                    "type": {
                        "type": "string",
                        "title": "Error Type"
                    }
                },
                "type": "object",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "title": "ValidationError"
            }
        }
    }
}


    return custom_api