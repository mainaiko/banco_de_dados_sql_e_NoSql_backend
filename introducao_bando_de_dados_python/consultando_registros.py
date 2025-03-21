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
# dados = [
#     ("kamille", "kamille@gmail"),
#     ("joao", "joao@gmail"),
#     ("maria", "maria@gmail"),
# ]

"""
consultas com um unico resultado
o metodo 'fetchone' pode ser usado para um unico registro de resultado. ele retorna o proximo registro 
na lista de resultados ou 'None' se nao houver mais resultados.
"""

def busca_unico_registro(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

"""
consultas com multiplos resultados
o metodo "fetchall()" pode ser usado para recuperar todos os registros de resultados de uma vez.
ele retorna uma lista de registros ou uma lista vazia se nao ouver mais resultados
"""

def busca_varios_registros(cursor):
    return cursor.execute("SELECT * FROM clientes;")


# cliente = busca_unico_registro(cursor, 1)
# print (cliente)

cliente = busca_varios_registros(cursor)
for clientes in cliente:
    print (clientes)
