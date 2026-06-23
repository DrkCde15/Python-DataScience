"""
SQLite: Cláusula ORDER BY.

Demonstra ordenação de resultados em ordem crescente (ASC)
e decrescente (DESC).
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com ORDER BY e exibe como DataFrame."""
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
SELECT nome FROM cliente ORDER BY nome;
'''
dml()

'''
SELECT nome FROM cliente ORDER BY nome ASC;
'''
dml()

'''
SELECT nome FROM cliente ORDER BY nome DESC;
'''
dml()