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

"""
operaçoes em lote
operaçoes em lote sao uteis quando precisamos inserir muitos registros de uma vez. com python DB API
podemos usar o metodo "executemany()" para isso
"""

def inserir_muitos_registro(con, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    con.commit()
dados = [
    ("kamille", "kamille@gmail"),
    ("joao", "joao@gmail"),
    ("maria", "maria@gmail"),
]
