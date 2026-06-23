"""
SQLite: Cláusula LIKE.

Demonstra busca de padrões em strings usando LIKE:
- '%a'  → termina com 'a'
- '%g'  → termina com 'g'
- '%a%' → contém 'a'
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com LIKE e exibe como DataFrame."""
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
SELECT nome FROM cliente WHERE nome LIKE 'a%';
'''
dml()

'''
SELECT modelo FROM tel WHERE modelo LIKE '%g';
'''
dml()

'''
SELECT modelo FROM tel WHERE modelo LIKE '%a%';
'''
dml()

'''
SELECT nome FROM cliente WHERE nome LIKE '%santos%';
'''
dml()