"""
SQLite: Cláusula WHERE.

Demonstra filtragem de registros com WHERE usando
comparações de igualdade, desigualdade e intervalos.
"""
import sqlite3
import pandas as pd


def dml():
    """Executa consulta SELECT com WHERE e exibe como DataFrame."""
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
SELECT * FROM cliente WHERE cidade = 'Sao Paulo';
'''
dml()

'''
SELECT modelo, valor FROM tel WHERE valor > 1000.0;
'''
dml()

'''
SELECT nome, sexo FROM cliente WHERE sexo = 'F';
'''
dml()

'''
SELECT * FROM cliente WHERE estado = 'RJ';
'''
dml()