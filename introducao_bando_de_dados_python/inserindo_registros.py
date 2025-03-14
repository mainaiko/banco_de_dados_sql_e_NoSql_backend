import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH/"meu_banco_de_dados.db")

cursor = con.cursor()
"""
inserindo registros
inserir registros em um banco de dados é uma operaçao comun. com python DB API, usamos a operaçao INSERT do SQL
"""

data = ("fatima", "fatima@gmail")
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
con.commit()
