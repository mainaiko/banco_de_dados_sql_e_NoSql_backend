"""
a DB API tambem nos permite gerenciar transaçoes, o que é essencial para manter
a integridade dos dados
"""
import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH/"meu_banco_de_dados.db")

cursor = con.cursor()

try:
    cursor.execute("INSERT INTO clientes VALUES (?, ?, ?)", (6, "teste", "teste"))
    con.commit()
except Exception as e:
    print (f"ocorreu um erro: {e}")
    con.rollback()
    
 
