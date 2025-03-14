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

"""
atualizando registros
a operaçao UPDATE SQL é usada para modificar registros existentes. é importante ser especifico
ao usar o UPDATE para evitar alterar mais registros do que o planejado
"""

def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    con.commit()

teste_1 = atualizar_registro(con, cursor, "Aiko Marques", "aiko@gmail.com", 1)

"""
removendo registros
a operaçao delete do SQL é usada para remover registros. novamente, precisamos ser especificos ao usar o delete para
evitar remover mais registros do que o planejado
"""

def remover_registro(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    con.commit()

