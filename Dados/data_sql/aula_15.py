"""
SQLite: Cláusula IN.

Demonstra filtragem por múltiplos valores possíveis
em uma mesma coluna usando IN.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa SELECT com IN e exibe como DataFrame."""
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
SELECT * FROM cliente WHERE cidade IN ('Rio de Janeiro', 'Niteroi');
'''
dml()

'''
SELECT * FROM tel WHERE valor IN (800.0, 1000.0, 1200.0);
'''
dml()