"""
SQLite: Cláusula LIMIT.

Demonstra como limitar a quantidade de registros
retornados por uma consulta SELECT.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com LIMIT e exibe como DataFrame."""
    con = sqlite3.connect('./table/loja.db')
    cur = con.cursor()

    query = input('Digite a Query desejada: ')
    cur.execute(query)

    registros = cur.fetchall()
    colunas = [desc[0] for desc in cur.description]

    df = pd.DataFrame(registros, columns=colunas)
    print(df)

    con.close()
    
'''
SELECT * FROM cliente LIMIT 1;
'''
dml()

'''
SELECT DISTINCT codcliente FROM cliente LIMIT 2;
'''
dml()