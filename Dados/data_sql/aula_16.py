"""
SQLite: Cláusula BETWEEN.

Demonstra filtragem por intervalo de valores
(inclusive) usando BETWEEN.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com BETWEEN e exibe como DataFrame."""
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
SELECT modelo, valor FROM tel WHERE valor BETWEEN 1000.0 AND 2000.0;
'''
dml()