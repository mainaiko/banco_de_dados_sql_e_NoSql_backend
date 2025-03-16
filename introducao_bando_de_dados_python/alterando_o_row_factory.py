import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH/"meu_banco_de_dados.db")

cursor = con.cursor()

def criar_tabela(con, cursor):
    nome_tabela = input(str(""))
    cursor.execute("CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150));", nome_tabela)
    con.commit()

def inserir_registro(con, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    con.commit()

def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()

def remover_registro(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    con.commit()

def inserir_muitos_registro(con, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    con.commit()

def busca_unico_registro(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

def busca_varios_registros(cursor):
    return cursor.execute("SELECT * FROM clientes;")

"""
trabalhando com resultados de consulta
os resultados das consultas sao retornados como tuplas por padrao. se a tupla nao atender 
as nossas necessidades podemos usar a classe "sqlite3.row" ou uma "row_factory" customizada
"""
def row_factory(cursor, id):
    cursor.row_factory = sqlite3.Row
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    result = cursor.fetchone()
    print(dict(result))

"""
codigo fica bem mais limpo e facil de manutençao dessa forma
colocar o row logo no inicio para todas as instancias serem iguais
"""
